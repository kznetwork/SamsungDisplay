from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def get_movie_reviews(url, max_reviews=100):
    driver = setup_driver()
    reviews = []
    
    try:
        logging.info(f"Accessing URL: {url}")
        driver.get(url)
        
        # Wait for the review tab and click it using the specific XPath
        review_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main_pack"]/div[3]/div[1]/div[3]/div/div/ul/li[8]/a/span'))
        )
        review_tab.click()
        logging.info("Clicked review tab")
        
        # Wait for reviews to load
        time.sleep(2)
        
        while len(reviews) < max_reviews:
            # Get review elements with updated selector
            review_elements = driver.find_elements(By.CSS_SELECTOR, "div.review_text, div.review_text_wrap")
            
            for element in review_elements:
                if len(reviews) >= max_reviews:
                    break
                    
                try:
                    review_text = element.text.strip()
                    if review_text and review_text not in reviews:
                        reviews.append(review_text)
                        logging.info(f"Collected review {len(reviews)}/{max_reviews}")
                except Exception as e:
                    logging.error(f"Error processing review: {str(e)}")
                    continue
            
            # Click more button if available
            try:
                more_button = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn_more"))
                )
                if more_button.is_displayed():
                    more_button.click()
                    time.sleep(1)
                else:
                    logging.info("No more reviews to load")
                    break
            except:
                logging.info("No more button found")
                break
                
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
    
    finally:
        driver.quit()
    
    return reviews

def save_reviews_to_csv(reviews, filename='movie_reviews.csv'):
    df = pd.DataFrame(reviews, columns=['review'])
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    logging.info(f"Saved {len(reviews)} reviews to {filename}")

if __name__ == "__main__":
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&pkid=68&os=11819814&qvt=0&query=%EB%AF%B8%EC%85%98%20%EC%9E%84%ED%8C%8C%EC%84%9C%EB%B8%94%20%ED%8C%8C%EC%9D%B4%EB%84%90%20%EB%A0%88%EC%BD%94%EB%8B%9D"
    reviews = get_movie_reviews(url, max_reviews=100)
    save_reviews_to_csv(reviews)
    print(f"총 {len(reviews)}개의 리뷰를 수집했습니다.")

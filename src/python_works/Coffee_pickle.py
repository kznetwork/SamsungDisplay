import pickle # pickle 모듈 가져다 쓰기

profile_file = open("MyModules/Coffee_pickle.pickle", "wb") # 바이너리(binary) 형태로 저장
profile = {"Coffee Shop":"My Coffee Shop", "Menu":["Coffee", "Tea", "Smoothie"]}
print(profile)

pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
profile_file.close()
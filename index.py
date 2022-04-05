cost = int(input("금액을 넣어주세요. : "))
while True:
  print("[이화네 음료수]")
  print("현재 금액 : " , cost, "원")
  ex = { "콜라":1000, "커피":400, "사이다":300, "율무차":200 }
  goods = list(ex.keys())
  ep = list(ex.values())
  for i in range(len(goods)):
    print(i+1 , "." , goods[i] , "-" , ep[i] , "원")
  for i in range(len(goods)):
    pick = int(input("음료를 선택해주세요. : "))
    if(pick>cost):
      print("돈이 부족합니다.")
      break
    else:
      print("잔액은 " , cost-ep[pick-1] , "원입니다.")
      answer = str(input("추가로 구매하시겠습니까? : "))
      if(answer != "Y"):
        print("이용해주셔서 감사합니다.")
        break



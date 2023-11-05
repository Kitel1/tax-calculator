#関数定義
def salesTax(price, reduce, include):
	""" 引数
	price : 購入金額
	reduce : True -> 軽減税率適用あり, False -> 軽減税率適用なし
	include : True -> 内税 Flase -> 外税
	"""
	#消費税率定義
	RATE08 = 0.08
	RATE10 = 0.1
	#関数内変数の初期化
	exprice = tax = taxrate = 0

	if price == 0:
		return False	

	if reduce == True:
		taxrate = RATE08
	elif reduce == False:
		taxrate =  RATE10
	else: 
		return False

	if include == True:
		exprice = price/(1+taxrate)
		exprice = round(exprice)
		tax=price-exprice
	elif include == False:
		exprice = price
		tax = price*taxrate
	else:
		return False

	return exprice, tax

#主処理

#購入金額の入力
uriage = int(input("購入金額："))
#軽減税率適用
temp = input("軽減税率適用？（Ｙ／Ｎ：")
if temp == "Y":
	keigen = True
else:
	keigen = False
#税込金額
zeikomi_input = input("税込金額？（Ｙ／Ｎ）：")
if zeikomi_input == "Y":
	zeikomi = True
else:
	zeikomi = False
	


zeinuki, tax = salesTax(uriage, keigen, zeikomi)
if zeinuki == False:
	print("入力エラー")
else:
	print("税抜き金額{0}円,　消費税{1}円".format(zeinuki, tax))
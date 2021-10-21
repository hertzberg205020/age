driving = input('請問你有沒有開過車\n')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = int(input('請問你的年齡\n'))

if driving == '有':
	if age >= 18:
		print('通過測驗')
	else :
		print('非法駕駛')
else :
	if age >= 18:
		print('快去考照')
	else :
		print('再等幾年')
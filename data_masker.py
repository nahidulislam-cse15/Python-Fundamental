cards=["1234567812345678","9876543298765432","1111222233334444"]
mask_ch="*"*12
#print(mask_ch)
masked_cards=[mask_ch+card[len(card)-4:] for card in cards]
print(masked_cards)


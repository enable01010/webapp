import streamlit as st
from random import randint

st.title("10連ガチャシミュレーションアプリ")
st.caption("ガチャを引くアプリです")

prob = [70,25,5]
sum_prob = sum(prob)

with st.form(key='gacha'):
	gacha_btn = st.form_submit_button("ガチャを引く")
	if gacha_btn == True:
		st.text("ガチャを引きました")
		for i in range(10):
			value = randint(1,sum_prob)
			rare = 1
			sum_p = 0
			for p in prob:
				sum_p += p
				if value <= sum_p:
					st.text("レア度"+"★"*rare + "を引いた")
					break;
				rare += 1
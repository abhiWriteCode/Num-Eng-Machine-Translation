from bs4 import BeautifulSoup
from requests import get
import random
import asyncio
import pandas as pd
from time import time


random.seed(12345)


async def convert2text(number):
	html_body = get('https://www.calculatorsoup.com/calculators/conversions/numberstowords.php?'
	                f'number={number}&format=words&letter_case=lowercase&action=solve')

	soup = BeautifulSoup(html_body.text, features="lxml")
	text = soup.find(id="answer").text

	return text


async def main(numbers):
	async def parallel_request(number):
		return (number, await convert2text(number))

	data = [parallel_request(number) for number in numbers]
	data = await asyncio.gather(*data)
	df = pd.DataFrame(data, columns=['number', 'text'])

	return df


if __name__ == '__main__':
	START_TIME = time()
	MIN = 500_000
	MAX = MIN + 500_000
	SAMPLE_PERCENTAGE = 1
	SAMPLE_SIZE = ((MAX - MIN) * SAMPLE_PERCENTAGE) // 100
	print(MIN, MAX, SAMPLE_SIZE)

	numbers = range(MIN, MAX)
	numbers = random.sample(numbers, k=SAMPLE_SIZE)
	df = asyncio.get_event_loop().run_until_complete(main(numbers))

	df.to_csv(f'data/num_text_pair - {MIN} - {MAX} - {SAMPLE_PERCENTAGE}.csv', index=False)
	print(f'required time: {time() - START_TIME:.2f} sec')
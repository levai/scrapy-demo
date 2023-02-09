import requests
import re
import pandas as pd


class FileInfo():
    def __int__(self):
        pass

    # 1.获取响应数据
    def get_res(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
        res = requests.get(url, headers)
        return res

    # 2.解析数据
    def parse_data_re(self, res):
        text = res.text
        file_names = re.findall('"m-b-sm">(.*?)</h2>', text)
        scores = re.findall('m-b-n-sm">\n(.*?)</p>', text)
        scores = [score.strip() for score in scores]
        return file_names, scores

    # 3.存储数据
    def save_excel(self, file_names, scores):
        df = pd.DataFrame()
        df['名称'] = file_names
        df['评分'] = scores
        print(df)
        df.to_excel("电影信息.xlsx", index=False)

    def main(self):
        file_names_list = []
        scores_list = []
        for num in range(1, 11):
            page_url = f"https://ssr1.scrape.center/page/{num}"
            print(page_url)
            res = self.get_res(page_url)
            file_names, scores = self.parse_data_re(res)
            file_names_list.extend(file_names)
            scores_list.extend(scores)
        self.save_excel(file_names_list, scores_list)


if __name__ == "__main__":
    fi = FileInfo()
    # url = "https://ssr1.scrape.center/page/2"
    # res = fi.get_res(url)
    # file_names, scores = fi.parse_data_re(res)
    # fi.save_excel(file_names, scores)
    fi.main()

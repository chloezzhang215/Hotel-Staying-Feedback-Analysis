import requests, time, csv
from bs4 import BeautifulSoup


url_list = []


headers = {'Referer':'https://www.booking.com/hotel/us/indigo-los-angeles-downtown.html?aid=304142;ucfs=1&',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

# for i in range(1,6):
    # params = {
    # 'aid': '304142',
    # 'label': 'gen173nr-1DCAso7AFCG2luZGlnby1sb3MtYW5nZWxlcy1kb3dudG93bkgzWARoiQKIAQGYATG4ARfIAQzYAQPoAQH4AQaIAgGoAgO4Auy7-IsGwAIB0gIkMzczNzA1OWEtODhmMS00NDVmLTg1ZjItZTQ3Mjk0N2MzZjBi2AIE4AIB',
    # 'sid': '42a1d99d02d86ba180f9f73b69ad4373',
    # 'cc1': 'us',
    # 'dist': '1',
    # 'length_of_stay': '1',
    # 'pagename': 'indigo-los-angeles-downtown',
    # 'type': 'total',
    # 'offset': str(i*10),
    # 'rows': '10',
    # '_': '1635655153109'
    # }
for i in range(1, 700):

    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=el-royale-near-universal-studios-hollywood&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637637320104'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=jolly-roger&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637638271985'
    #url = ' https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=hollywood-inn-express-north&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637640125542'
    #url = ' https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=sofitel-los-angeles&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637642228569'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=kimpton-everly&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637647237662'
    #url = ' https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=hollywood-the-of-hollywood&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637648057187'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=venice-on-the-beach-venice&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637649058539'
    #url = ' https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=level-furnished-living&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637650818847'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=friendship-motor-inn&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637652141165'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=days-inn-studio-city&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637652986072'
    #url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=hostelling-international&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637653749570'
    #url = ' https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=banana-bungalow-west-hollywood&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637654330107'
    # url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=super-8-los-angeles-airport-lax&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637654941422'
    url = 'https://www.booking.com/reviewlist.html?aid=304142;label=gen173nr-1DCAEoggI46AdIM1gEaIkCiAEBmAEruAEHyAEN2AED6AEBiAIBqAIDuAKA_OeMBsACAdICJDU1MWVmNzJlLTE1NjEtNDc1YS1iN2QyLWVlNmJkNjAwMzNmYtgCBOACAQ;sid=08b2e3d123f840696c87d000952ebe3c;srpvid=ca849d3386ba0058;sig=v1EC2A7cQC&;cc1=us&pagename=days-inn-hollywood-walk-of-fame&r_lang=&review_topic_category_id=&type=total&score=&sort=&dist=1&offset='+str(i*10)+'&rows=10&rurl=&text=&translate=&time_of_year=&_=1637655755199'



    res = requests.get(url, headers = headers)

    print(res.status_code)

    bs = BeautifulSoup(res.text, 'html.parser')
    score_list = bs.find_all('div', class_="bui-review-score__badge")
    comment_list = bs.find_all('div',class_="bui-grid__column-10")
    message_list = bs.find_all('div',class_="c-review")
    
    scores = []
    for i in score_list:
        scores.append(i.text)


    titles = []
    for comment in comment_list:
        title = comment.find_all('h3')
        for i in title:
            titles.append(i.text.replace('\n', ''))

    contents = []
    for message in message_list:
        content = message.find_all('span')
        # print(content)
        inner_list = []
        for i in content:
        
            review = i.text.replace('·','').replace('Liked','').replace('Disliked','').replace('\xa0', '').strip()
            if review != "This review has been hidden because it doesn't meet our guidelines." and review != '':

                inner_list.append(review)
        if len(inner_list) != 0:
            contents.append(inner_list)

    review_dict = {}
    for i in range(len(titles)):
        if len(titles) == len(contents):
        
            review_dict[titles[i]] = [contents[i],scores[i]]

    # print(review_dict)

    with open('booking90.com.csv', 'a', encoding= 'utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for i in review_dict:
            if len(review_dict[i][0]) != 1:
                writer.writerow([i,review_dict[i][0][0], review_dict[i][0][1], review_dict[i][1]]) 
            else:   
                writer.writerow([i,review_dict[i][0][0], ' ', review_dict[i][1]]) 

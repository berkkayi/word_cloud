



def main(arg="words"):
        
    import pandas as pd
    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
    import matplotlib.pyplot as plt
    from PIL import Image

    def convert(text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text


    items = {".":"",
            ",":"",
            ",":" ",
            "?":"", 
            '"':'', 
            ":":"",
            ";":""}


    with open('file.txt') as a:
        file = a.read()
    
    
    file = convert(file,items)
    b = pd.Series(file.split()).str.lower().value_counts()

    data = pd.DataFrame({"values":b.index,
                        "count":b}).reset_index().drop("index",axis=1)


    data["values"] = data["values"].astype(str)
    data["values"] = data["values"].replace(" ","")


    with open("turkce-stop-words") as a:
        file = a.read()
    stop = file.split("\n")
    data = data[~data["values"].isin(stop)]


    txt = ",".join(list(data["values"].values))

    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="black").generate(txt)
    wordcloud.to_file(f"{arg}.png")

if __name__ == "__main__":
        
    import sys
    
    i, arg = enumerate(sys.argv)
    main(sys.argv[1:][0])

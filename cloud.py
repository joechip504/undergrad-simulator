from wordcloud import WordCloud

if __name__ == '__main__':
    cloud = WordCloud(
        font_path="/Library/Fonts/Verdana.ttf",
        width=1000,
        height=1000,
    )

    [cloud.stopwords.add(w) for w in ["sent", "iphone"]]

    text = open('undergrads.txt').read()
    cloud.generate(text).to_file('undergrads-1.png')

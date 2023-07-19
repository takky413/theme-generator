from flask import Flask
app = Flask(__name__)

# もともとmain.pyにあったコードを以下に移動（import app 以外）
from flask import render_template, redirect, url_for
import random


@app.route('/')
def index():
    return render_template(
        'index.html',
    )
    
    

@app.route('/interview')
def interview():
    themes = ["自己紹介をしてください",
              "志望動機を教えてください", 
              "自己PRをしてください",
              "あなたの長所を教えてください",
              "あなたの短所を教えてください",
              "これまでの人生で、何かに向かって努力した経験を聞かせてください",
              "これまでの人生において、もっとも大きな挫折の経験を教えてください",
              "就活の軸を教えてください",
              "学生時代に頑張ったことを教えてください",
              "入社後にしたいことを教えてください",
              "挫折経験を教えてください",
              "尊敬する人がいれば教えてください",
              "他社の選考状況を教えてください",
              "最後に何か質問はありますか",
              "最近気になるニュースは何ですか",
              "アルバイト経験について教えてください",
              "キャリアプランについて教えてください",
              "あなたの趣味は何ですか",
              "自分を動物に例えると何ですか",
              "業界の志望理由を教えてください",
              "苦手な人はどんなタイプですか",
              "学生と社会人の違いは何だと思いますか",
              "好きな言葉・座右の銘は何ですか"
              ]
    theme = random.choice(themes)
    
    return render_template(
        'interview.html',
        theme = theme
    )

@app.route('/reload_interview', methods=["GET"])
def reload_interview():
    return redirect(url_for('interview'))


@app.route('/group_discussion')
def group_discussion():
    themes = ["外国人観光客の一人当たり支出額を増加させるにはどうすればいいか", 
              "新幹線の新しいサービスを考案せよ",
              "日本人が海外に誇れる強み3つあげて発表せよ",
              "リーダーに必要なものは何か",
              "いい本とはどんな本か",
              "物を売る際に必要な力は何か",
              "良い鉄道とは何か",
              "うどんとそば、世界に売り出すならどちらか",
              "新規牛丼店を出店する際にどのような店にするか",
              "最新IT技術を用いて、働きやすい環境を考えよ",
              "待機児童を減少させるには",
              "高齢化が進む中で、ウェアラブル端末はどのような役割を果たすべきか",
              "和傘を普及させるためには",
              "テクノロジーを用いて家事の負担を軽減する新しいアイデアを提案してください",
              "ある企業で女性の労働者数を増やすには",
              "キャッシュレス化を推進するためには",
              "高校の定員割れを解決するには",
              "コンサルタントに必要な3つの資質は何か",
              "売上が伸び悩んでいるチェーンの本屋に対し売上向上策を提案せよ",
              "花屋の売上を上げる施策を考えよ",
              "フィットネスクラブの会員数を増やすには",
              "デパートのエレベーターの混雑を解消するにはどうすればよいか"              
              ]
    theme = random.choice(themes)
    
    return render_template(
        'group_discussion.html',
        theme = theme
    )

@app.route('/reload_group_discussion', methods=["GET"])
def reload_group_discussion():
    return redirect(url_for('group_discussion'))


@app.route('/case')
def case():
    themes = ["ガソリンスタンドの売上を向上させる施策を考えてください", 
              "タクシー会社の売上を向上させる施策を考えてください",
              "選挙の投票率を上げる施策を考えてください",
              "映画館の売上を向上させる施策を考えてください",
              "缶コーヒーの市場規模を拡大させる施策を考えてください",
              "違法駐車を減らす施策を考えてください",
              "ゲームセンターの市場規模を拡大させる施策を考えてください",
              "水泳教室の売上を向上させる施策を考えてください",
              "カラオケボックスの売上を向上させる施策を考えてください",
              "あるラーメン屋一店舗の売上を向上させる施策を考えてください",
              "パン屋の客数減少の理由を特定してください",
              "東京都内の交通渋滞を緩和する施策を考えてください",
              "文房具店の売上を向上させる施策を考えてください",
              "野菜ジュースの売上を向上させる施策を考えてください"
              ]
    theme = random.choice(themes)
    
    return render_template(
        'case.html',
        theme = theme
    )

@app.route('/reload_case', methods=["GET"])
def reload_case():
    return redirect(url_for('case'))


@app.route('/fermi')
def fermi():
    themes = ["カフェの市場規模を推定せよ", 
              "日本のとあるカフェ1店舗の売上を推定せよ",
              "カフェへの来客数を推定せよ",
              "日本に存在するカフェの数を推定せよ",
              "東京都のカフェ市場の売上を推定せよ",
              "スターバックス全店の売上を推定せよ",
              "缶ビールの市場規模を求めよ",
              "日本国内にあるキャリーケースの数を推定せよ",
              "日本国内にある携帯電話の数を推定せよ",
              "カラオケボックスの市場規模を推定せよ",
              "東京都内にタクシーは何台あるか",
              "あるラーメン屋一店舗の売上を推定せよ"
              ]
    theme = random.choice(themes)
    
    return render_template(
        'fermi.html',
        theme = theme
    )

@app.route('/reload_fermi', methods=["GET"])
def reload_fermi():
    return redirect(url_for('fermi'))


@app.route('/back', methods=["GET"])
def back():
    return redirect(url_for('index'))
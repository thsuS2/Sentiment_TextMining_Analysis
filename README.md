# Sentiment_TextMining_Analysis
텍스트 마이닝 기반의 감성 분석 연구

텍스트 마이닝 기반의 감성 분석 연구 (Sentiment analysis study based on text mining) (2019년도 Python으로 개발된 졸업작품 입니다.)

📌텍스트마이닝이란? 데이터 마이닝의 일종으로, 텍스트 기반의 데이터베이스로부터 사용자가 관심을 가지는 정보들을 자동적으로 추출하는 프로세스를 말합니다. 또 감성분석이란, 글에서 인상, 감정, 태도, 의견과 같은 감성을 추출하고 분석하는 연구 분야로, 주로 마케팅, 여론분석, 소셜 미디어 컨설팅 분야에서 사용되고 있습니다.

📌개요 빅데이터의 시대가 도래함에 따라, 사용자들이 데이터를 단순 소비하는 방식을 넘어 적극적으로 생산하고있는 시대가 되었습니다. 이에 따라 소셜 데이터의 가치 또한 커졌습니다. 기존의 감성 분석 서비스들에는 사용자 의견 조사나, 업체 평판 모니터링 등의 서비스를 제공하는 어@비 소셜 예측 퍼블리싱, 아이@엠 소셜 애널리틱스, s@플래닛 스마트인사이트 등이 있습니다. 해외에서는 감성 분석을 이용하여 대선 기간동안 선거 전략에 사용하는 등의 많은 활용 사례가 존재하지만, 국내에는 이제 도입 단계라고 합니다. 그러나 이러한 기존의 소셜 데이터들을 다루는 텍스트 마이닝 분야에서는 기존 분석 결과의 정확성이 떨어지고, 분석 내용은 긍정인지 부정인지의 단순한 극성 파악 수준에 일상언어, 신조어가 포함된 소셜 미디어의 분석의 신뢰도가 낮고, 다양한 감성을 분석할 수 있는 능력이 없다는 점에서 이러한 연구가 필요하다고 판단하였습니다.

📌개발 목표 텍스트 마이닝의 단순한 긍정 부정 분석을 넘어서 다양한 감성 분석 기능을 강화하는 것이고, 또한신조어가 포함된 소셜 미디어의 분석 결과의 정확도를 향상시키는 것 입니다. 연구 내용은 먼저 감성 단어 사전에 신조어를 추가해 감성 단어 사전을 보완하고, 감성 모델에 추가 감성 단어를 배치하고, 기존 단어의 위치를 재조정 하고, 소셜 미디어용 크롤러의 제작, 워드 매칭 알고리즘의 개선, 그리고 마지막으로 분석 결과의 시각화 까지 구현하는 것을 목표로 개발하였습니다.

📌개발 방법 및 내용 크게 댓글 크롤러, 형태소 분석기, 감성단어사전 세가지 부분으로 나누어 개발하였습니다. 프로그램 흐름은 아래와 같이 진행됩니다.
1. 댓글 크롤러를 이용해 인터넷 기사에서 기사 댓글을 수집
2. 수집한 기사 댓글을 형태소 분석기를 이용하여 표제어를 추출
3. 추출한 표제어는 감성 단어 사전을 이용하여 감성단어를 필터링 및 빈도수 측정 / 감성 모델에 맵핑하여 시각화

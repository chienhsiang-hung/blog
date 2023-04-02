---
title: "H&M Personalized Fashion Recommendations"
date: 2023-03-22T09:30:00+08:00
lastmod: 2023-03-22T09:49:00+08:00
draft: true
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
images: ["posts/2023/"]
featuredimage: 
tags: [""]
toc:
  enable: true
zhtw: true
---
## 目錄
1. 選題原由
2. 建模內容與成效說明
3. 發現
4. 應用場景

## 題目
[H&M Personalized Fashion Recommendations | Kaggle](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/overview)

> Provide product recommendations based on previous purchases

根據客戶過去**一段時間內**的<mark>商品購買紀錄</mark>以及<mark>商品資訊(文字、圖片)</mark>精準<mark>預測未來一週內可能購買的商品</mark>。可以延伸分析**不同客群對商品組合的偏好**、**客戶CLTV**等。

## 筆記
<object data="H&M%20Personalized%20Fashion%20Recommendations.pdf" type="application/pdf" width="100%" height="600px">
    <embed src="H&M%20Personalized%20Fashion%20Recommendations.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="H&M%20Personalized%20Fashion%20Recommendations.pdf">Download PDF</a>.</p>
    </embed>
</object>

### 選題原由
第一題是推薦系統，第二題是進銷存系統

以金融業的商業模式來說，推薦系統會是更值得優先投入的領域

## 問題、資料與模型
預測12個最好的候選推薦，從105542個articles

我們知道這類ranking問題可以用LGBM, XGBoost, CatBoost等來處理

但要根據每個使用者特徵對10萬個商品預測排序似乎不太實際，因此我們還需要在前一步加filter，或者說-選出候選人（召回）

初步的流程就會是從pool召回百個到千個，然後再排序出前12個。因為排序是從召回的候選人來進行，因此，要是前面召回不夠精準，後面排序模型再準確也沒用，那麼召回流程就至關重要。

關鍵問題就來了，我們該如何來進行召回呢？怎麼做才能從10萬筆項目中找出有效候選人（候選項目）？

## 資料集data
首先我們來看看我們手上有哪些資料集
- 商品圖庫
- 商品敘述(主要為文字): 商品分類、顏色、款式及用戶群(男女老幼)等
- 顧客資料: 區域、年齡及是否接受電子行銷等
- 顧客消費紀錄: 顧客、價格與通路等

## 資料處理與特徵
資料量有多少呢（35GB）

10萬種產品、3千萬筆交易
- negative samples 數量太多

  Downsampling to 可以隨機抽樣，一到兩百萬個每週(for all customers)有比較好的performance
### 召回方法
- 過去購買過（商品、類別）
- collaborative filtering
- 上一週熱門產品
- 去年同期熱門產品
- graph embedding（圖片分類）
- logistic regression on 類別資訊（分類、款式等）
- 平均購買價格（）
![平均購買價格.jpeg](平均購買價格.jpeg "平均購買價格.jpeg")



### 特徵
- 顧客商品購買次數、顧客分類購買次數 (周月季/去年同期(周)/全期/時間加權)

### 訓練與測試

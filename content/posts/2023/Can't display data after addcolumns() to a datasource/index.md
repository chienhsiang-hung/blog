---
title: "Can't display data after addcolumns() to a datasource"
date: 2023-03-09T12:32:00+08:00
lastmod: 2023-03-09T12:32:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "I am able to see the table is generated successfully though the addColumns() generated columns (total_aum, total_income) couldn’t be displayed in a gallery or anywhere in the canvas app. fx: First(table).total_income should display 0 not blank()."
images: ["posts/2023/cant-display-data-after-addcolumns-to-a-datasource/Explicit-column-selection.png"]
featuredimage: Explicit-column-selection.png
tags: ["Powerapps", "Connecting to Data", "Creating Apps", "General Questions", "Using Apps Using Formulas"]
toc:
  enable: true
---
## Problem
[Re: Can't display data after addcolumns() to a dat... - Power Platform Community (microsoft.com)](https://powerusers.microsoft.com/t5/Building-Power-Apps/Can-t-display-data-after-addcolumns-to-a-datasource/m-p/2049326)

Here is the table:

```markup
With(
    {
        isnotteamhead: First(colSession).CurrLevel <> "RO",
        isnotbanker: First(colSession).CurrLevel <> "Banker",
        ro: First(colSession).CurrTeam,
        banker: First(colSession).CurrBanker
    },
    Search(
        AddColumns(
            GroupBy(
                Filter(
                    WAM_Trade_Summarizes,
                    FinalDate_yyyymm in ComboBoxTradeFinalDate.SelectedItems,

                    (isnotteamhead || RO_gb=ro),
                    (isnotbanker || GroupBanker_gb=banker)
                ),
                "crfb8_statement_prod_type_gb", "rest"
            ),
            "total_income", Sum(rest, Final_Rev_gb),
            "total_aum", Sum(rest, Total_amount_gb)
        ),
        SearchTypeRevenue.Text, "crfb8_statement_prod_type_gb"
    )
)
```

It looks like this:

![chienhsianghung_0-1678161411320.png](https://powerusers.microsoft.com/t5/image/serverpage/image-id/615547i89C224F112FC695B/is-moderation-mode/true/image-dimensions/2500?v=v2&px=-1 "chienhsianghung_0-1678161411320.png")

I am able to see the table is generated successfully though the `addColumns()` generated columns (`total_aum`, `total_income`) couldn't be displayed in a gallery or anywhere in the canvas app.

fx: `First(table).total_income` should display 0 not blank().

![chienhsianghung_1-1678161630961.png](https://powerusers.microsoft.com/t5/image/serverpage/image-id/615548iB2E47792B268EF82/is-moderation-mode/true/image-dimensions/2500?v=v2&px=-1 "chienhsianghung_1-1678161630961.png")

Same when I try to retrieve data within a gallery.

![chienhsianghung_2-1678161724177.png](https://powerusers.microsoft.com/t5/image/serverpage/image-id/615549i5BFC8E39607C3B6A/is-moderation-mode/true/image-dimensions/2500?v=v2&px=-1 "chienhsianghung_2-1678161724177.png")

Has anyone faced a similar situation? I'm stuck :dizzy_face:


Even weirder now when I tested it with Label. In the Ideas, it showed Current formate xxxxxx.xx means the data was fetched successfully. But it just wouldn't show. So confused :dizzy_face:

![chienhsianghung_1-1678262752202.png](https://powerusers.microsoft.com/t5/image/serverpage/image-id/616343iEDE867B9736607B6/is-moderation-mode/true/image-dimensions/2500?v=v2&px=-1 "chienhsianghung_1-1678262752202.png")

## Solution
![Explicit-column-selection.png](Explicit-column-selection.png "Explicit-column-selection.png")
Then I found the problem is because of the **Explicit column selection** feature again.

When I tried to calculate the `total_income` number in the gallery.
```
Sum(
    Thisitem.rest, revenue
)
```
The data was able to be **retrieved** and **displayed** successfully. So I figured the problem would be 
>`AddColumns()` wouldn't be considered

when you have **Explicit column selection** ticked.

Below is the trick I used to retrieve the needed data at the first steps of `With()` instead of using `ShowColumns()` to explicitly select columns but still able to tell the power apps to load the data.
```
With(
    {
        userlevel_isnot_banker: First(colSession).UserLevel <> "Banker",
        isnotteamhead: First(colSession).CurrLevel <> "RO",
        isnotbanker: First(colSession).CurrLevel <> "Banker",
        ro: First(colSession).CurrTeam,
        banker: First(colSession).CurrBanker,
        fetch_Final_Rev_gb: First(WAM_Trade_Summarizes).Final_Rev_gb,
        fetch_Total_amount_gb: First(WAM_Trade_Summarizes).Total_amount_gb
    },
    Search(
        AddColumns(
            GroupBy(
                Filter(
                    WAM_Trade_Summarizes,
                    FinalDate_yyyymm in ComboBoxTradeFinalDate.SelectedItems,

                    (isnotteamhead || RO_gb=ro),
                    (isnotbanker || GroupBanker_gb=banker),

                    (userlevel_isnot_banker || (
                        Statement_prod_type_gb <> "Extra Rate" &&
                        Statement_prod_type_gb <> "Management fee" &&
                        Statement_prod_type_gb <> "Error"
                    ))
                ),
                "crfb8_statement_prod_type_gb", "rest"
            ),
            "total_income", Sum(rest, Final_Rev_gb),
            "total_aum", Sum(rest, Total_amount_gb)
        ),
        SearchTypeRevenue.Text, "crfb8_statement_prod_type_gb"
    )
)
```
Notice, I use `fetch_Final_Rev_gb: First(WAM_Trade_Summarizes).Final_Rev_gb`, `fetch_Total_amount_gb: First(WAM_Trade_Summarizes).Total_amount_gb` to achieve the goal.
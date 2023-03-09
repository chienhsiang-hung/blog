---
title: "PowerApps `not in`"
date: 2023-03-09T11:39:00+08:00
lastmod: 2023-03-09T11:39:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
featuredimage: featured-image.jpg
tags: ["Powerapps", "not in", "Operators", "Powerplatform", "Microsoft"]
toc:
  enable: false
---
![Photo by Sigmund on Unsplash](https://miro.medium.com/v2/resize:fit:700/0*KtRj-F_dd2-whbep "Photo by Sigmund on Unsplash")

“not operator along with the custom named condition operators is not allowed”

Operator <> or NOT In. In and Exactin

For example in an  `Items`  of  `Gallery`  :
```
With(  
    {  
        userlevel_isnot_banker: First(colSession).UserLevel <> "Banker",  
        isnotteamhead: First(colSession).CurrLevel <> "RO",  
        isnotbanker: First(colSession).CurrLevel <> "Banker",  
        ro: First(colSession).CurrTeam,  
        banker: First(colSession).CurrBanker,  
    },  
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
    )  
)
```
Use this
```
(  
            Statement_prod_type_gb <> "Extra Rate" &&  
            Statement_prod_type_gb <> "Management fee" &&  
            Statement_prod_type_gb <> "Error"  
        )
```
instead of
```
!(Statement_prod_type_gb in ["Extra Rate", "Management fee", "Error"])
```
or
```
Not(Statement_prod_type_gb in ["Extra Rate", "Management fee", "Error"])
```
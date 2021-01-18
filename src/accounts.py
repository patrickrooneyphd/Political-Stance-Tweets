#
# accounts.py
#
# Desc: Lists of all accounts to scrape
#

ceos = {"sundarpichai": "ALPHABET INC", "JeffBezos": "AMAZON.COM INC", "tim_cook": "APPLE INC",
        "ChuckRobbins": "CISCO SYSTEMS INC", "LarryMerloCVS": "CVS HEALTH CORP", "MichaelDell": "DELL TECHNOLOGIES INC",
        "RobertIger": "DISNEY (WALT) CO", "JimFitterling": "DOW INC",
        "mtbarra": "GENERAL MOTORS CO",
        "MarvinREllison": "LOWE'S COS INC",
        "satyanadella": "MICROSOFT CORP", "ramonlaguarta": "PEPSICO INC", "AlbertBourla": "PFIZER INC",
        "hansvestberg": "VERIZON COMMUNICATIONS INC"
        }
#
companies = {"abbvie": "ABBVIE INC", "Allstate": "ALLSTATE CORP", "Google": "ALPHABET INC",
             "amazon": "AMAZON.COM INC", "AmericanAir": "AMERICAN AIRLINES GROUP INC",
             "AmericanExpress": "AMERICAN EXPRESS CO", "AIGinsurance": "AMERICAN INTERNATIONAL GROUP",
             "Healthcare_ABC": "AMERISOURCEBERGEN CORP", "AnthemInc": "ANTHEM INC",
             "ADMupdates": "ARCHER-DANIELS-MIDLAND CO", "ATT": "AT&T INC", "BankofAmerica": "BANK OF AMERICA CORP",
             "BestBuy": "BEST BUY CO INC", "Boeing": "BOEING CO", "CapitalOne": "CAPITAL ONE FINANCIAL CORP",
             "cardinalhealth": "CARDINAL HEALTH INC", "CATERPILLAR INC": "CaterpillarInc", "Centene": "CENTENE CORP",
             "GetSpectrum": "CHARTER COMMUNICATIONS INC", "Chevron": "CHEVRON CORP", "Cigna": "CIGNA CORP",
             "Cisco": "CISCO SYSTEMS INC", "Citi": "CITIGROUP INC", "CocaColaCo": "COCA-COLA CO",
             "comcast": "COMCAST CORP", "conocophillips": "CONOCOPHILLIPS", "Costco": "COSTCO WHOLESALE CORP",
             "CVSHealth": "CVS HEALTH CORP", "JohnDeere": "DEERE & CO", "DellTech": "DELL TECHNOLOGIES INC",
             "Dell": "DELL TECHNOLOGIES INC", "Delta": "DELTA AIR LINES INC", "WaltDisneyCo": "DISNEY (WALT) CO",
             "DowNewsroom": "DOW INC", "Exelon": "EXELON CORP", "exxonmobil": "EXXON MOBIL CORP",
             "Facebook": "FACEBOOK INC", "FreddieMac": "FEDERAL HOME LOAN MORTG CORP",
             "FannieMae": "FEDERAL NATIONAL MORTGA ASSN", "Ford": "FORD MOTOR CO",
             "generaldynamics": "GENERAL DYNAMICS CORP", "generalelectric": "GENERAL ELECTRIC CO",
             "GM": "GENERAL MOTORS CO", "GoldmanSachs": "GOLDMAN SACHS GROUP INC",
             "HCAhealthcare": "HCA HEALTHCARE INC", "HelmerichPayne": "HELMERICH & PAYNE",
             "HomeDepot": "HOME DEPOT INC", "honeywell": "HONEYWELL INTERNATIONAL INC", "Humana": "HUMANA INC",
             "intel": "INTEL CORP", "IBM": "INTL BUSINESS MACHINES CORP", "JNJNews": "JOHNSON & JOHNSON",
             "jpmorgan": "JPMORGAN CHASE & CO", "kroger": "KROGER CO", "LockheedMartin": "LOCKHEED MARTIN CORP",
             "Lowes": "LOWE'S COS INC", "MarathonPetroCo": "MARATHON PETROLEUM CORP", "McKesson": "MCKESSON CORP",
             "Merck": "MERCK & CO", "MetLife": "METLIFE INC", "Microsoft": "MICROSOFT CORP",
             "MorganStanley": "MORGAN STANLEY", "northropgrumman": "NORTHROP GRUMMAN CORP", "PepsiCo": "PEPSICO INC",
             "pfizer": "PFIZER INC", "Phillips66Co": "PHILLIPS 66", "ProcterGamble": "PROCTER AND GAMBLE CO",
             "progressive": "PROGRESSIVE CORP-OHIO", "Prudential": "PRUDENTIAL FINANCIAL INC",
             "RaytheonTech": "RAYTHEON CO", "Sysco": "SYSCO CORP", "Target": "TARGET CORP",
             "Tech_Data": "TECH DATA CORP", "tjmaxx": "TJX COS INC (THE)", "TysonFoods": "TYSON FOODS INC  -CL A",
             "united": "UNITED AIRLINES HOLDINGS INC", "UPS": "UNITED PARCEL SERVICE INC",
             "UnitedHealthGrp": "UNITEDHEALTH GROUP INC", "ValeroEnergy": "VALERO ENERGY CORP",
             "Verizon": "VERIZON COMMUNICATIONS INC", "WBA_Global": "WALGREENS BOOTS ALLIANCE INC",
             "WalmartInc": "WALMART INC", "WellsFargo": "WELLS FARGO & CO",
            }

combined_accounts = dict()
combined_accounts.update(ceos)
combined_accounts.update(companies)


empty_ceo_accounts = {"larryculpjr": "GENERAL ELECTRIC CO", "DavidSolomon": "GOLDMAN SACHS GROUP INC",
                      "Samuel_HazenHCA": "HCA HEALTHCARE INC", "GinniRometty": "INTL BUSINESS MACHINES CORP",
                      "BruceDBroussard": "HUMANA INC", "BobSwan": "INTEL CORP",
                      "TysonFoodsCEO": "TYSON FOODS INC  -CL A", "CarolBTome": "UNITED PARCEL SERVICE INC",
                      }

empty_company_accounts = {"Apple": "APPLE INC", "world_fuel": "WORLD FUEL SERVICES CORP"}

# Interesting Notes:
# GOOG has public policy team (@googlepubpolicy)
# ABC has an advocacy Twitter handle (@Advocacy_ABC)
# AAPL (@Apple) twitter account is empty-- they only buy ads on twitter
# CVS (@CVSinAction) is a local community service oriented account
# XOM (@XOMFoundation) is an account for the company's philanthropic arm
# Ford (@FordFund) is an account for the company's philanthropic arm
# Home Depot (@HomeDepotFound) is an account for the company's philanthropic arm
# NGC (@NGCNews) is an account for press releases and events, separate from @northropgrumman
# PEP (@Pepsi) is a separate verified account that seems to revolve around marketing deals to consumers.
# PSX (@phillips66media) is the news media account
# PRU (@PrudentialNews) is the news media account of Lauren Day, Chief Comms Officer
# TGT (@TargetNews) is the news media account
# TJX has separate twitter accounts for @tjmaxx, @marshalls, and @HomeGoods, using @tjmaxx as the flagship brand
# VZ has separate policy (@VerizonPolicy) and news (@VerizonNews) accounts
# WBA has separate Walgreens (@Walgreens) and news (@WalgreensNews) accounts
# WMT has separate Walmart (@Walmart), social impact (@WalmartAction), and philanthropy (@WalmartOrg) accounts

# CEOs Notes:
# BOE: Dave Calhoun, started Jan 13, 2020, on Boeing Board of Dirs since 2009, VP at Blackstone prior to CEO, no Twitter
# @finkd is Mark Zuckerberg's twitter, which is still active but has around 10 posts, most from 2009.
# MPC: Michael Hennigan is new CEO as of Mar 18, 2020, joined in 2017.
# RTX: Raytheon Greg Hayes is new CEO as of April 2020, when he joined the company
# SYY: Sysco CEO is Thomas Bené, not Thomas Ben as printed in STATA.
# UAL: New CEO Scott Kirby started in early May 2020, and he joined the company as President on Aug 29, 2016
# UPS: New CEO Carol Tomé started as CEO on June 1, 2020 when she joined from Home Depot. Old CEO Abney no TWTR
# WF: New CEO Charles Scharf became CEO on Oct 21, 2019. Joined directly from Visa.
# NOTE! WF CEO Scharf made negative comments about black talent in June 2020 internal memo (Forbes)



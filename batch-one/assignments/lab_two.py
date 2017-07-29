#!/usr/bin/python3

data_string = '''
| 2017-01-01 - 07:01:43 | JawaharlalNehru | view | Main.WebHome | Mozilla | 253.111.182.73 | 
| 2017-01-01 - 07:01:48 | AlbertEinstein | view | Main.WebHome | Mozilla | 201.36.26.7 | 
| 2017-01-01 - 07:04:39 | BillGates | view | Main.TWikiPreferences | Mozilla | 45.47.246.39 | 
| 2017-01-01 - 07:17:49 | QueenElizabeth | view | TWiki.TWikiPreferences | Mozilla | 235.40.131.35 | 
| 2017-01-01 - 07:19:50 | ThomasEdison | view | TWiki.ManagingWebs | Mozilla | 253.111.182.73 | 
| 2017-01-01 - 07:21:38 | FranklindRoosevelt | view | Main.WebHome | Mozilla | 226.223.113.236 | 
| 2017-01-01 - 07:43:10 | DesmondTutu | view | Fullgc.WebHome | Mozilla | 84.216.7.151 | 
| 2017-01-01 - 07:54:57 | BenazirBhutto | edit | Fullgc.WebHome |  | 171.155.32.163 | 
| 2017-01-01 - 08:02:42 | AbrahamLincoln | view | Fullgc.WebHome | Mozilla | 155.248.2.129 | 
| 2017-01-01 - 08:08:30 | ElvisPresley | view | Fullgc.WorkLog | Mozilla (not exist) | 197.72.39.116 | 
| 2017-01-01 - 08:10:34 | WaltDisney | view | Fullgc.WorkLog | Mozilla (not exist) | 137.129.127.164 | 
| 2017-01-01 - 08:12:41 | CharlesDarwin | edit | Fullgc.WorkLog | (not exist) | 41.80.213.179 | 
| 2017-01-01 - 08:21:20 | AbrahamLincoln | edit | Fullgc.WorkLog | (not exist) | 89.235.198.102 | 
| 2017-01-01 - 08:21:23 | MikhailGorbachev | save | Fullgc.WorkLog |  | 199.168.5.94 | 
| 2017-01-01 - 08:25:50 | QueenVictoria | view | Fullgc.WorkLog | Mozilla | 97.51.168.65 | 
| 2017-01-01 - 08:30:48 | LeonardodaVinci | edit | Fullgc.WorkLog |  | 143.132.190.10 | 
| 2017-01-01 - 08:34:17 | RichardBranson | save | Fullgc.WorkLog | repRev 1 by BaseUserMapping_333 2016/07/02 08:12:09 | 191.237.243.148 | 
| 2017-01-01 - 08:44:50 | LudwigBeethoven | view | Fullgc.WorkLog | Mozilla | 144.161.226.230 | 
| 2017-01-01 - 08:47:51 | JohnfKennedy | edit | Fullgc.WorkLog |  | 171.155.32.163 | 
| 2017-01-01 - 08:48:19 | MarilynMonroe | save | Fullgc.WorkLog | repRev 1 by BaseUserMapping_333 2016/07/02 08:33:01 | 94.167.29.154 | 
| 2017-01-01 - 09:00:00 | PabloPicasso | view | Fullgc.WorkLog | Mozilla | 228.87.151.113 | 
| 2017-01-01 - 09:06:20 | AbrahamLincoln | view | Fullgc.BlogEntryOne | Mozilla (not exist) | 183.223.63.105 | 
| 2017-01-01 - 09:10:54 | MikhailGorbachev | view | Fullgc.BlogEntryOne | Mozilla (not exist) | 209.0.136.148 | 
| 2017-01-01 - 09:19:40 | PeterSellers | edit | Fullgc.BlogEntryOne | (not exist) | 243.57.27.87 | 
| 2017-01-01 - 09:23:03 | RosaParks | save | Fullgc.BlogEntryOne |  | 221.156.0.8 | 
| 2017-01-01 - 09:25:04 | AlbertEinstein | view | Fullgc.BlogEntryOne | Mozilla | 75.131.57.87 |

'''

a = data_string.split('\n')


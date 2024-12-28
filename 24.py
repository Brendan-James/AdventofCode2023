import math
from sympy import *
#import vpython
data = """181562673221791, 338272173381384, 367757712264029 @ 54, -10, -10
206315329209944, 245384073975106, 327941392745372 @ 55, 100, 14
197625997051112, 364791147875511, 421084289548856 @ 13, -27, -52
335607631675402, 372977327877226, 443503801516025 @ -91, -180, -307
376965726440887, 243145753709446, 134693184039803 @ -60, -103, 438
275283382407707, 271946025294316, 261942712309417 @ -31, 55, 99
184473941815821, 260190025352516, 334809258307979 @ 46, 90, 35
248747432562397, 292825978198210, 296262988127717 @ 33, 9, 27
233282077872895, 269698571568655, 349260681338282 @ -12, 77, 14
289832617329133, 247310128837201, 364857887373709 @ -78, 103, -15
176510447686183, 285361628169508, 268796009216369 @ 92, 45, 101
173077274557783, 342809180288503, 381193797311774 @ 12, 17, 22
338197337823745, 208688417067388, 262562967802577 @ -19, 136, -59
124016688125887, 256968737904589, 372750640778267 @ 68, 105, 27
325149428756895, 361379049392837, 209001310210807 @ -76, -145, 163
253976258556295, 193124198162056, 312138083232833 @ 70, 178, -44
378596236273183, 231895538890288, 254905382141909 @ -48, -62, -373
224973520218728, 220472972985443, 228282364691207 @ 67, 131, 143
346972455220783, 376128181087648, 219089567689529 @ -128, -142, 153
194891381248987, 341939810732800, 298055964752030 @ 136, -82, 16
268631000175487, 260391421511819, 271165340356205 @ 36, 47, 41
390961594308071, 175701973054280, 191639068825713 @ -95, 398, -6
239282117255637, 302971698559003, 273253909331433 @ 130, -59, 13
375169157673286, 440906377097719, 455688520466693 @ -171, -305, -319
389354581104375, 259046365255576, 261631061379501 @ -80, -422, -692
363909741820838, 143727477234489, 196962106286293 @ 157, 693, -47
134058908931127, 109573327969703, 122711220866454 @ 300, 341, 330
345378216612978, 230029990821320, 233232686321991 @ 17, 38, -33
346278365905713, 268060717608134, 148345178285689 @ -98, 12, 285
301993883158924, 202646196395387, 422059457827578 @ -21, 159, -272
302900291580407, 113811588900180, 360050527110785 @ -52, 314, -91
314215338670581, 442661597371898, 286777787001103 @ -115, -139, 94
73485654784612, 227444244495455, 142532185860807 @ 135, 135, 271
191716102992463, 316513954730740, 207404598033569 @ 82, -5, 185
353480547346623, 229708640151188, 184123612031809 @ 34, 9, 153
287651081353953, 260151513044618, 339842520020129 @ -115, 107, 77
384859152975880, 219516961898458, 169601357797985 @ 51, -124, 197
289181142397513, 358109881230418, 239297076804479 @ -75, -45, 148
246011259732974, 180495865234476, 222295339641605 @ 145, 210, 113
362933947846827, 224445185589322, 215528822021969 @ -26, 43, 5
334864957684888, 258063592787374, 236116581601097 @ -13, -16, 29
335128154699797, 193103990705438, 406941878080253 @ -114, 176, -151
212650469710183, 173522809994728, 154756338204449 @ 56, 204, 262
261155597759258, 365250285781953, 339523838631449 @ 149, -271, -211
188487353621487, 424903026405464, 89908157766377 @ 103, -180, 362
378853791124582, 292485330206872, 214681378464893 @ -171, -42, 137
79393850811029, 66353436972592, 257807145798867 @ 95, 298, 154
323162994624628, 169156971144598, 257265211113059 @ 113, 292, -137
393490001855158, 258916912837279, 212763818527253 @ -103, -517, -287
361156978649963, 215281182789768, 234252868642873 @ -13, 86, -93
250930306653319, 442285474209160, 356991679892369 @ -55, -108, 30
88004022065719, 136973968591396, 264540373062065 @ 184, 247, 117
139077199481279, 356838817208182, 339399214073987 @ 80, -17, 44
366640498293653, 221423485959773, 189593402985354 @ 178, -73, -6
156654429837175, 101556474710683, 130551672108656 @ 140, 311, 298
138318009435529, 307691006876284, 263548888956727 @ 81, 40, 132
378038785142823, 285671133485900, 216282012604045 @ 92, -883, -362
334035885160323, 252690527170293, 271456260979054 @ -32, 17, -48
382557369761690, 282195328751976, 551282074313802 @ -169, -58, -794
398273440484414, 201600550955163, 207827305534891 @ -139, 131, -357
304516112424581, 394419094999880, 170048858432959 @ -97, -90, 240
259085529690193, 305070703342915, 351713138988821 @ -18, 13, -23
369242901604373, 159257820378672, 233649329129337 @ -13, 410, -167
117204084588568, 255618305428272, 486710786403131 @ 57, 110, -73
336323444417107, 515990495084812, 384349605461733 @ -159, -155, 24
277141878029502, 269529496734636, 199322609696582 @ 199, -70, 134
37278090617617, 400751841530176, 53109952757069 @ 129, -30, 355
390656376510277, 226936458359803, 179409553991787 @ -42, -209, 67
313924500640943, 344700606232488, 186680344644369 @ 73, -318, 177
244177571012887, 54844281180643, 263442967729094 @ 44, 411, 80
337738511704075, 247897587947056, 296408930569673 @ -61, 44, -81
358491244805179, 262611133333524, 379487313971339 @ -144, 50, -145
209668825493704, 224943482402203, 196118461963568 @ -39, 141, 216
473597262632155, 519964022034006, 413095048545753 @ -330, -307, -119
263618584034062, 173766584423278, 222150504812279 @ 49, 216, 135
392315256982015, 240757814243320, 217405344790193 @ -175, -16, 21
232908143971513, 337546851929608, 364413849397124 @ 10, -26, -30
525394990446403, 486670295779072, 549078392958317 @ -398, -238, -293
234382681247081, 328299708132154, 327808628474887 @ 13, -17, 16
146252896929473, 316607902867069, 212872709179305 @ 82, 25, 189
238753528445991, 301523936325192, 313245539488689 @ 65, -15, -15
379599462590599, 302611228873528, 350338902550697 @ -192, 16, -22
177995307124885, 210334085263090, 151690006346429 @ 239, 143, 275
226636375324317, 398568597830488, 308298286204598 @ -14, -74, 74
241928920505863, 377248173876682, 209567229958961 @ 12, -97, 181
302730427045063, 299784821461276, 282818195904053 @ 52, -111, -76
228977965957329, 121751658702074, 507323095001897 @ -49, 245, -103
495910176566635, 482206100683476, 554657540616761 @ -399, -363, -481
270639052697059, 306549937334560, 328991147970461 @ -71, 40, 54
321016938512446, 399773998262441, 200913171105597 @ 51, -505, 129
138854573610383, 157304431697138, 160107154636109 @ 32, 207, 251
308977105957547, 344965272037946, 309403544522603 @ -82, -57, 26
311963302471675, 251158010804226, 72731835458733 @ 126, -33, 603
258627550256334, 331560553246532, 310241572618852 @ -65, 18, 84
227079488302827, 119641914726680, 229949219151565 @ 209, 362, 88
474181220024151, 414865393462576, 482997748923369 @ -326, -137, -200
237805279666763, 369307253718380, 472284936813691 @ -38, -28, -104
336759161010693, 276803626371752, 232366858131303 @ 37, -138, -14
285260173131958, 366410057542153, 391876112481349 @ 129, -335, -431
215308893104317, 326724080962126, 357548117279546 @ 30, -8, -16
213853230177364, 230169283668988, 358354128875021 @ 141, 106, -127
281937306006151, 430233809413552, 360402312751427 @ -52, -166, -34
306835778244187, 234809283449844, 343595407786483 @ -102, 120, 16
388068293128213, 212557280152243, 184427972700104 @ 30, -45, -42
255550659347143, 293261084062138, 469148228566079 @ -84, 75, -48
279777638558533, 305379745666033, 324285166980194 @ 22, -47, -72
302060306499868, 442163096469403, 345110770534454 @ -129, -69, 72
301859458999952, 454991102465631, 273986564796659 @ 29, -475, -25
198074216132137, 336747869633692, 544540598576600 @ -30, 34, -118
179482776920027, 389114872312318, 286898605054085 @ 74, -89, 83
368264434084857, 306774350011220, 328505421828673 @ -187, 44, 61
381662263968518, 330120005642029, 216040118582723 @ -143, -323, 59
29347732679711, 157804089779856, 51444115078017 @ 334, 228, 417
370353488300455, 153268402815880, 125510914636145 @ 74, 573, 606
265746162850023, 157917802294536, 29927073740241 @ 182, 288, 648
11647101799117, 162535934305885, 282752708757437 @ 190, 205, 121
384167640680809, 262925268463405, 208730867313567 @ -126, -155, 31
275289388506595, 263748923788522, 348444473677688 @ 8, 48, -88
234038042849869, 457165486197504, 487751837993437 @ -51, -102, -89
254453428808928, 292510744582503, 331008389074609 @ 5, 21, -11
383137119835921, 233137479438565, 467269952359583 @ -186, 99, -349
181760957373223, 267990993803608, 367249421310449 @ 60, 77, -15
342772317506088, 195571130616858, 218599497922764 @ 11, 180, 42
138942685211892, 449967672146504, 495391271341505 @ 43, -90, -91
301178023158675, 259094298872206, 246118132832953 @ 46, 7, 33
290565171346003, 407230592360926, 128973285080921 @ -8, -236, 317
477116240993767, 470774794888896, 427731635821497 @ -300, -103, -14
109545436412263, 259670007959368, 382142687867889 @ 123, 94, -12
348248514871399, 281933169835784, 181940162117937 @ -135, 29, 219
314973602170582, 235418052483559, 181439399604269 @ 125, 23, 185
339762780094493, 468346787359298, 532389389674554 @ -142, -192, -242
418194346655359, 284109595217980, 281767190056581 @ -246, 55, 94
325008844018295, 241016344159319, 224377691134267 @ -116, 107, 163
215063995257423, 453094802604638, 25077578126217 @ -8, -129, 409
297655058139175, 437184572786200, 395340507795137 @ -84, -155, -64
275782564110463, 350911437632408, 375357794956041 @ -33, -64, -72
283524676320025, 298993321012891, 242148150234911 @ 30, -47, 83
232808088065018, 360592624334734, 418555025020417 @ -43, -8, -27
360465350422135, 469334972231223, 543533428734061 @ -180, -129, -167
352493378430108, 316790635233868, 173110748805544 @ 127, -638, 198
178545257717657, 163566952073460, 520515932732957 @ 13, 204, -133
238622167508965, 325544724359299, 369059196008405 @ -22, 9, -7
381732176697238, 333471354286378, 490381319232749 @ -179, -124, -455
197836133386367, 393355764529216, 302777621166657 @ 5, -53, 91
349414437329575, 331413048189928, 310631476308545 @ -124, -84, -28
342925370215135, 205238954109810, 242175124384231 @ 36, 140, -81
158341181539593, 317053254319498, 519848112291959 @ 10, 52, -97
172336601699083, 140450521256608, 234914085186599 @ 262, 290, 100
325795215781031, 163192740468680, 141478402991537 @ 115, 323, 353
301184910771447, 189964800349398, 421564011414330 @ -116, 176, -32
335404433020573, 271012214104291, 287656094202674 @ 42, -115, -230
369518048114439, 147932065059856, 201262870860809 @ 56, 583, -40
367738950407451, 188113367998556, 146201553101741 @ 173, 287, 464
273041709059871, 297441919966400, 314728914987805 @ 10, -12, -24
388785487173919, 252236154432538, 246374687731802 @ -172, -24, -42
247095302306473, 451720384398568, 319489521315839 @ 81, -330, -56
278698871724849, 297362268529986, 298178681913155 @ 55, -55, -52
293517508833898, 467241849979216, 273836958407597 @ 7, -402, 17
176691514023941, 339396886160277, 478659797457181 @ 14, 17, -87
166646025315307, 51015825615109, 356989056460004 @ 40, 333, 30
295432611181257, 296558530640775, 327933569262472 @ -106, 57, 64
330909894634863, 160696485880764, 256180323071857 @ -58, 255, 37
360981046820951, 295008888190528, 402607570071129 @ -160, 16, -125
348599369845813, 180358394690473, 361616157158144 @ -142, 195, -56
187382695347900, 358211504358469, 377274223963338 @ -11, 7, 34
297100785896473, 361564660079284, 227828901644453 @ -113, -8, 179
392137063734825, 299219958096586, 498816543820612 @ -214, 52, -134
212648689915833, 316816804277753, 306606070954099 @ -34, 47, 103
211897485766688, 125364598177218, 52516278257939 @ -35, 240, 359
253334290981897, 329667593677375, 382184771211480 @ -30, -5, -38
381397310569621, 276400631798203, 174097859147597 @ -146, -109, 217
325469710354783, 149442252855178, 254662625711249 @ -128, 229, 133
338435179067033, 302962292249253, 330003862689074 @ -118, -7, -28
385509049211627, 196359546693248, 193053043271709 @ -94, 186, 55
225414204613431, 390679542524072, 405607031741929 @ -56, -18, 15
56444408557739, 359215078247360, 254625767271319 @ 146, -6, 150
114146919608837, 249959478431248, 316027932255743 @ 115, 106, 68
246484409318791, 426404502945808, 416552416677425 @ -16, -139, -91
284935770377263, 273745776723268, 265344685720409 @ 30, 5, 31
220077701171338, 325732557809347, 383463419063795 @ -43, 39, 27
362151858233807, 206555195393668, 232099004238793 @ -142, 151, 111
252432730962015, 298686441963920, 325879440146401 @ 50, -16, -47
287942559663714, 354948336670754, 342678438141105 @ -59, -60, -11
293522684984110, 153125729519572, 418335482032145 @ -45, 242, -171
346906753506595, 281426989889192, 207913628261849 @ -21, -130, 95
222886755293765, 257597357839013, 304634084384035 @ -26, 101, 91
294137222562768, 347145072005183, 398580160837729 @ 53, -211, -347
363991000342723, 258828715029868, 226882702944839 @ -26, -132, -58
316113875021047, 387339744337303, 181288227406079 @ -52, -209, 215
85169943338149, 158252632188898, 271743568168393 @ 123, 211, 129
374754843671533, 290304131541553, 200645941214124 @ 66, -737, -96
236858791766869, 207021662923000, 398472888001007 @ -57, 158, 8
477790855923425, 445806604910074, 444682290300059 @ -311, -113, -70
36199112714433, 176405734422628, 213307481936469 @ 257, 196, 183
323650134777512, 232351259308564, 235644486758691 @ 35, 58, 19
382218564326725, 474223171168840, 488549009722349 @ -197, -218, -205
277246970102952, 423693200033652, 350959692808389 @ -49, -150, -15
368718657703880, 325220851461441, 218715803759251 @ -145, -127, 123
280456979016416, 295657592013586, 352443076764976 @ 11, -20, -114
353365084417931, 273004117328300, 282984476661573 @ -71, -61, -114
295385769127233, 249537517652742, 241966520688111 @ 47, 39, 54
117029536337869, 128557913697954, 74633545638055 @ 183, 267, 376
251065809958073, 332751051365998, 346305930533773 @ -73, 31, 63
396702255812503, 185479221077506, 162311248886715 @ -108, 379, 306
300950201597555, 218912294398963, 371426221668413 @ 8, 121, -223
224583045524239, 184021557373699, 279158011432265 @ 116, 195, 29
132543142424320, 255981713381203, 332089546886732 @ 131, 91, 26
235661473763113, 435835647537948, 375731932387529 @ -54, -78, 29
206638737514159, 256729647290796, 330496628639513 @ 126, 63, -49
255271607034503, 352570435747358, 385724555207019 @ -52, -15, -14
345946570243108, 227250816843532, 313594668007670 @ -153, 130, 56
309528177535174, 354584076911218, 250879943089841 @ 59, -304, -11
379675588587743, 325135035782104, 170843664465353 @ -83, -572, 218
330624129007722, 273633757888786, 208032878486257 @ -115, 52, 181
360127736167375, 218609903770528, 207162851638433 @ -57, 91, 87
259798653308935, 279528942541288, 386092914824225 @ -30, 56, -56
382274411158675, 222770911836604, 181361080431713 @ 18, -96, 77
405229454274093, 422743644825798, 307474676343499 @ -229, -111, 70
184756211133524, 294347250779949, 378746555678138 @ 79, 33, -52
281347495913585, 247764619751743, 231937269029475 @ 38, 61, 103
67633758847546, 418047861629040, 190763664737115 @ 129, -66, 219
366857240216119, 211419557942364, 193413447520915 @ 36, 80, 54
269323363106844, 230970433583796, 188854028791732 @ -7, 114, 208
251132051577109, 256535953026738, 268950586329136 @ 66, 56, 48
431708442743601, 480981657374807, 347358684331834 @ -286, -433, -140
389940153875353, 215946698026450, 185720811341573 @ -63, -25, 23
221497196692783, 312839941218384, 211113285858193 @ 147, -67, 153
295373443737508, 341465321067563, 409258972816319 @ -123, 29, 11
200679737239621, 289138975337789, 431339365713144 @ 114, 15, -200
302246913072295, 342511897137432, 329432559226209 @ -84, -36, 15
337646379823599, 272258047357752, 233956579910379 @ -16, -66, 30
326581481861968, 141499538760838, 320366811392054 @ 23, 352, -252
189175907276623, 106844816257384, 223634700153425 @ 117, 314, 153
52783206135183, 230544843278068, 30331855809309 @ 142, 133, 388
231655584127975, 469961149868704, 309100487876321 @ -20, -160, 73
339660238746910, 104133525911393, 210376998262650 @ -27, 461, 108
333891529416679, 165019053118237, 303623850172587 @ -36, 259, -129
88474161805051, 308669435255548, 268423512975961 @ 75, 61, 147
200134884340159, 342775811471084, 206204933810045 @ 48, -28, 191
85618651407848, 313918989290028, 226062562018044 @ 161, 26, 172
367509375194167, 210900843346568, 206371204619641 @ 24, 86, -29
375399894354145, 201402729997332, 139750647179787 @ -45, 152, 412
322112034541223, 221689164469503, 307063488893504 @ -100, 131, 26
425908195333157, 361112157033454, 315064257850425 @ -269, -143, -39
336264513930631, 140254281081307, 269892387982751 @ 60, 415, -193
359636285197451, 512685053178252, 546583173295173 @ -161, -303, -324
301904496873968, 103340136497887, 266369382865859 @ -13, 367, 35
298873350505415, 435026421476712, 266734473398097 @ -19, -301, 46
338904952534645, 332756709035814, 308951886170131 @ -99, -97, -36
126175931952567, 333114487100476, 319894125305025 @ 40, 37, 97
305951648841283, 145351767871548, 229256906491889 @ 147, 371, 5
161712155293336, 483649246568839, 326302596664361 @ 51, -161, 61
218248515024183, 64564409838648, 249297825610209 @ 97, 401, 100
363010690349858, 320609910413403, 345218343205874 @ -169, -7, -10
331171892395977, 381482501959370, 160177331824047 @ -95, -165, 256
378778712998425, 227998503763454, 196241369480838 @ -34, -52, 18
147700329930034, 307438714679533, 437391857646012 @ 21, 61, -18
212578859471635, 359871870588240, 390872920128277 @ 6, -30, -29
403605482006842, 280054746223087, 335332301438036 @ -225, -131, -376
311614529896315, 259401261197308, 201422331355373 @ 165, -89, 96
108439815976871, 297176656319784, 333225801809473 @ 68, 68, 78
371362533663556, 269087589744637, 171282946219589 @ -97, -111, 225
204877587519379, 329600848084132, 256560765124097 @ 205, -117, 49
281678544938368, 294135204488683, 285273997393376 @ 37, -39, -12
362462482588136, 278508065281757, 238823191853996 @ -91, -93, 8
336955832566795, 293165672910568, 214569881035121 @ -27, -114, 101
318204074740069, 363964133945587, 139242062639432 @ -14, -243, 312
233460248814566, 289074064433762, 176316947023193 @ 179, -48, 221
321715541839165, 239591705201682, 303325049203835 @ 210, -48, -481
193548422710679, 421664122813368, 384848087336577 @ -10, -64, 19
271559476052183, 26971674712308, 391080546693649 @ 32, 503, -195
364105457245316, 297489433694190, 387150255130849 @ -155, -12, -155
240713136245418, 185234110289583, 313060070890249 @ -5, 185, 45
241978914402883, 394318914010028, 456386224403649 @ -69, -25, -39
262386277491969, 406773649091810, 89754667253503 @ 58, -252, 399
307069700983153, 147864742857968, 333772800691589 @ -99, 234, 23
178735495965199, 360257339978869, 408303019671827 @ 20, -11, -21
95234686392118, 308051335117303, 93946690006640 @ 127, 41, 328
349497189535627, 231319507064998, 348540510187937 @ -134, 111, -67
158696725579811, 337006410972392, 510795592265409 @ 43, 14, -135
312297019934263, 361653503937913, 331961143546679 @ 140, -483, -417
298615497463903, 125438244269648, 433157535620219 @ -96, 258, -88
324729480059363, 219105654507033, 253688107619552 @ 152, 71, -172
343467015094791, 244144552233432, 253745811179089 @ -26, 17, -45
391227279742375, 251413012754168, 361962875010801 @ -204, 71, -111
174995604143874, 258326442515151, 358616163305337 @ 125, 75, -51
289002530729367, 324141104381304, 315995273793921 @ 14, -96, -69
265828905902401, 539640298481149, 367095741147049 @ -90, -173, 45
356629952209303, 298929840518704, 134785145366417 @ 82, -481, 449
361751647429693, 172459349665508, 281317299062219 @ -129, 228, -22
233421154923641, 106516965872622, 270364876350531 @ 130, 360, 27
237096607105559, 273152663353338, 315196386108985 @ 100, 21, -47
311965007999883, 147648817121328, 476953020148749 @ -106, 234, -165
200813075189027, 345579199625860, 315997853920053 @ 14, -8, 67
118653140744943, 337457866486528, 451083039437525 @ 82, 16, -64
296937765493903, 292868339836918, 270089014148579 @ 68, -92, -41
375453900653303, 334247938352891, 281385324209507 @ -148, -207, -73
340166802203683, 456204718506328, 517568527274699 @ -166, -82, -94
247209284795147, 331572400925832, 233558950908507 @ 190, -186, 66
309868299452903, 245599885818760, 409497488879313 @ -118, 112, -38""".split("\n")

data2 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3""".split("\n")

data = [[[int(k) for k in j.split(", ")] for j in i.split(" @ ")] for i in data]

testarea = (200000000000000,400000000000000)
testarea2 = (7,27)

extra = []

for i in data:
	x,y,z = i[0]
	vx,vy,vz = i[1]
	slope = vy/vx
	yintercept = (-(x/vx))*vy+y
	extra.append([slope,yintercept])

def intersect(a,b):
	global extra
	global data
	global testarea
	metaslope = extra[a][0]-extra[b][0]
	if metaslope == 0:
		return False
	metaintercept = extra[a][1]-extra[b][1]
	x = -metaintercept/metaslope
	y = extra[a][0]*(-metaintercept/metaslope)+extra[a][1]
	if not testarea[0]<x<testarea[1] or not testarea[0]<y<testarea[1]:
		return False
	if (data[a][0][0]>x and data[a][1][0]>0) or (data[a][0][0]<x and data[a][1][0]<0) or (data[b][0][0]>x and data[b][1][0]>0) or (data[b][0][0]<x and data[b][1][0]<0):
		return False
	return True

total = 0
for i in range(len(data)):
	for j in range(i+1,len(data)):
		if intersect(i,j):
			total+=1

print(total)

""" # visualization
for i in data[:3]:
	x,y,z = i[0]
	dx,dy,dz = i[1]
	normal = math.sqrt(dx**2+dy**2+dz**2)
	normal /= 300000000000000
	dx /= normal
	dy /= normal
	dz /= normal
	vpython.arrow(pos=vpython.vector(x,y,z),axis=vpython.vector(+dx,+dy,+dz),round=True,shaftwidth=1000000000000,headwidth=1500000000000,headlength=1000000000000)
"""

x, y, z, vx, vy, vz = symbols('x, y, z, vx, vy, vz', real=True)

equations = []

for i,v in enumerate(data[:5]):
	xn,yn,zn = v[0]
	vxn,vyn,vzn = v[1]
	tx = symbols("t"+str(i),real=True)
	equations.append(Eq(x+vx*tx,xn+vxn*tx))
	equations.append(Eq(y+vy*tx,yn+vyn*tx))
	equations.append(Eq(z+vz*tx,zn+vzn*tx))

# the magic box tells me the answer
print(solve(equations,domain=S.Reals))

print(404422374079783+199182431001928+166235642339249)
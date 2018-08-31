/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50520
Source Host           : localhost:3306
Source Database       : library

Target Server Type    : MYSQL
Target Server Version : 50520
File Encoding         : 65001

Date: 2018-08-29 08:37:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `admin`
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `uname` varchar(32) DEFAULT NULL,
  `upass` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES ('abc', '900150983cd24fb0d6963f7d28e17f72');

-- ----------------------------
-- Table structure for `arc`
-- ----------------------------
DROP TABLE IF EXISTS `arc`;
CREATE TABLE `arc` (
  `bookid` int(30) DEFAULT NULL,
  `flagid` varchar(50) DEFAULT NULL,
  `id` int(30) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of arc
-- ----------------------------
INSERT INTO `arc` VALUES ('10', '1,2', '3');
INSERT INTO `arc` VALUES ('11', '1,2', '4');

-- ----------------------------
-- Table structure for `bigtype`
-- ----------------------------
DROP TABLE IF EXISTS `bigtype`;
CREATE TABLE `bigtype` (
  `id` tinyint(20) NOT NULL AUTO_INCREMENT,
  `bigtyname` varchar(20) DEFAULT NULL COMMENT '大分类名字',
  `bigtyid` tinyint(20) DEFAULT NULL COMMENT '大分类id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bigtype
-- ----------------------------
INSERT INTO `bigtype` VALUES ('9', '女生专区', '1');
INSERT INTO `bigtype` VALUES ('10', '男生专区', '2');
INSERT INTO `bigtype` VALUES ('11', '文科', '3');
INSERT INTO `bigtype` VALUES ('12', '理科', '4');
INSERT INTO `bigtype` VALUES ('13', '其他', '5');
INSERT INTO `bigtype` VALUES ('14', '综合', '6');

-- ----------------------------
-- Table structure for `book`
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `tyniid` int(30) DEFAULT NULL,
  `bookimg` varchar(500) DEFAULT NULL,
  `introinfo` varchar(100) DEFAULT NULL COMMENT '书介绍',
  `author` varchar(50) DEFAULT NULL COMMENT '作者名',
  `bookname` varchar(50) DEFAULT NULL COMMENT '书名',
  `bookid` int(255) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`bookid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of book
-- ----------------------------
INSERT INTO `book` VALUES ('5', 'static/image/book/6331534080458646.jpg', '111111111111111111111111111111111111', '六月观主', '封仙', '10');
INSERT INTO `book` VALUES ('2', 'static/image/book/5671534080468631.jpg', 'sadasddsadasdasdaa', '金庸', '神雕侠侣', '11');

-- ----------------------------
-- Table structure for `cat`
-- ----------------------------
DROP TABLE IF EXISTS `cat`;
CREATE TABLE `cat` (
  `catinfo` varchar(20000) DEFAULT NULL COMMENT '每一章内容',
  `bookid` tinyint(10) DEFAULT NULL COMMENT '书id',
  `catname` varchar(30) DEFAULT NULL COMMENT '章节名',
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `catid` int(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of cat
-- ----------------------------
INSERT INTO `cat` VALUES ('当今天地，已至沉稳之机，须得定下诸天神灵，分雷火瘟斗，三山五岳，群星列宿，兴云布雨，幽冥善恶等八部正神，掌控天地秩序。\r\n　　至此，众仙共立封神榜。\r\n　　事涉天地万古秩序，波及众生，致使凡尘俗世，亦滋生战事。\r\n　　俗世王朝更迭，战火兴盛，各方依附着修道之人，最终让这天下尘世家国之战，演化为封神战场。\r\n　　在这其中，将以气运高低，道行深浅，缘法亲疏等缘故，封立各方身殒的修道之人以及俗世凡人。\r\n　　自前朝大唐分裂以来，当前天地各处，尽出烽火狼烟。\r\n　　时至今日，天下三分，互相制衡，局势勉强稳定。\r\n　　南为梁国。\r\n　　中土则为蜀国。\r\n　　北部往上则称元蒙国。\r\n　　……\r\n　　“人之初，性本善。”\r\n　　“性相近，习相远。”\r\n　　傍晚时分，天边一片昏黄金光。\r\n　　读书声从瓦房中传来，声音稚嫩，又显驳杂。\r\n　　过了片刻，才听一声清朗声音道：“今日到此为止，天色晚了，回家去罢。”\r\n　　然后几声欢呼的孩童声音，也有好学的孩子发出少许几分意犹未尽的声音。随后七八个孩童跑出房外，临走前不忘朝后面挥手：“先生，明天见。”\r\n　　房门处站有一人，面带笑容，怀中抱着一卷书。\r\n　　这人一身淡色白衣，清逸脱俗。\r\n　　五官端正，相貌清朗，约有十八九岁。\r\n　　细看之间，便觉他面上带两分笑意，眉宇深藏少许茫然。\r\n　　他名为清原，当年曾是上界仙宫弟子，因没有根骨，遂而下界，寻访机缘，可至今一无所得。\r\n　　饶是他静修多年，耐得住枯燥，已是心境平和，但至今全无所得，难免迷茫惘然。\r\n　　静立片刻，终是叹了一声，转回屋内。\r\n　　日落西山，晚霞渐去。\r\n　　入夜，深沉。\r\n　　屋中亮起烛光，从窗子边上，能够看见一个影子端坐桌前，翻阅起了一本书籍。\r\n　　“天之道，损有余而补不足。仙之道……”\r\n　　他声音清朗，字字清晰。\r\n　　……\r\n　　月光皎洁，薄如轻纱。\r\n　　人已入睡。\r\n　　“大仙门下道童清原，不守戒律，擅自翻阅仙根册，窥探封神榜，并私服九牛二虎之宝，畏罪而逃，今奉命诛之！”\r\n　　寂静而朦胧的夜间，一道清脆冷漠的声音忽然响起。\r\n　　隐约间，似有一行人推开了木门。\r\n　　皎洁的月光下，人影虚幻，似有似无，飘然如仙。\r\n　　身后是数名道童，均是清秀俊逸之辈，道气氤氲，灵意盎然。\r\n　　当头那个，也是个童子，约十二三岁，白衣出尘，眉宇高傲，面色冷漠，手执玉如意在怀，背负仙剑，在数丈外伸指点了过来。\r\n　　“白鹤师兄……”\r\n　　清原蓦然惊醒，浑身凉透。\r\n　　他深吸口气，惊魂未定。\r\n　　“又是恶梦……”\r\n　　当年他是紫霄仙宫童子，偶然之间，发现了记载天下修行根骨的仙根册，上面却无自家姓名，自知是福薄命薄无仙根。\r\n　　想要去寻大仙解惑，却得知大仙闭关。\r\n　　而回到炼丹房，又发现大仙交代的九牛二虎之面塑，已经烧毁了。\r\n　　他在仙宫多年，一心修仙，经此事后，惊觉自己全无根骨，思绪不免恍惚，心灰意冷。\r\n　　哪怕是根骨低劣，资质愚钝，但日夜苦修，付出十倍努力，想来，总是勤能补拙。然而，他却是全无根骨，不论如何刻苦修行，都一无所得。\r\n　　纵有神仙真传，但却无法修行，连修道的第一道门也无法推开。百年之后，便该如寻常人一般，寿尽而亡了。\r\n　　后来他在迷茫间，风吹倒了九牛二虎面塑，倒向南方。\r\n　　南斗主生，北斗主死。\r\n　　清原身在仙宫，熟读道书，认为这是异象，于是仔细思忖，留在仙宫亦是空耗光阴，只得下界寻访机缘。\r\n　　而临行时，带走了那段时日间一直揣摩的《黄庭仙经》，带走了在烧炼丹药时用来捣火的铁棒，并吃下了那半生不熟，几乎已是毁去的九牛二虎面塑。\r\n　　“算了算，也有数年之久了。”\r\n　　清原怅然一叹。\r\n　　他自下界之后，一直往南行走，数年来竭力摸索机缘，也历经无数艰险。\r\n　　想这数年间，躲过虎狼，避过树妖，伤于木魅，逃出魍魉妖魔之手，亦多次险些丢了性命。\r\n　　直到踏足黎村，才得以安宁一段日子。\r\n　　黎村是中原蜀国南部边境的一座村落，若是再往南行，便要越过前方的深山老林，去往南梁国。\r\n　　那深山密林间，凶禽猛兽众多，传闻亦有妖物精怪，常人无法行走。\r\n　　可若是要绕过这里，一则路途遥远。二来，则是两国交界，大军对峙之地，不得来往。\r\n　　于是停步在此，已有多日。\r\n　　这些时日间，他受村中葛老先生所邀，教孩童识字，也借此来平复自身心境。\r\n　　清原心中叹了声，抬头望向窗外，能见天上明月，心中忖道：“今夜是十三，待到十五，便又是大仙讲法之日了。”\r\n　　他悠悠一叹，沉入观想之中。\r\n　　意想头顶生出一个明月，遂而一分为六。\r\n　　六月光照，宛如梦幻。\r\n　　月光洒落，薄如轻纱，清凉如水。\r\n　　照澈出眉宇中的九重玉楼。\r\n　　……\r\n　　深夜。\r\n　　月色朦胧。\r\n　　这夜间，忽然一声尖叫，显得凄厉可怕。\r\n　　声音传遍了整座村落。\r\n　　清原蓦然惊醒，他翻身下来，顺手拾起一旁的铁棒，奔出房外。\r\n　　“怎么回事？”\r\n　　那里已经有人赶到，出声询问。\r\n　　适才那惊叫声的主人，喘息未定，说道：“葛老先生……”\r\n　　清原见他脸色惨白，又带着些惶恐之态，心知不好，连忙赶去。\r\n　　那处房屋之中，床边倒着一个老人，胸腹间的衣衫被扯裂，五道深可见骨的伤口，并排斜下，触目惊心。\r\n　　他气若游丝，但勉强未死。\r\n　　与此同时，村中其余人也纷纷赶至。\r\n　　纷纷扰扰，忙成一团，村中并无郎中，众人竟束手无策。\r\n　　清原见葛老先生伤势较重，思索片刻，说道：“我来试试。”\r\n　　当年在天上仙宫之内，他曾是为大仙烧炼丹药的童子。\r\n　　为了避免炼丹之时出错，曾翻阅过许多药材典籍，因而识得诸般药理，期间不免也涉猎了几分岐黄医术。\r\n　　听闻清原开口，众人面面相觑，略有惊讶，但终究是让了开来。\r\n　　村里没有郎中，须得到镇上去请，然而一来一回，这葛老先生多半是撑不住了。\r\n　　清原这年轻人，数月前来到村中，能教村中孩童读书，性子温和平淡，严谨而谦逊，又是个识字的书生。\r\n　　识字之人，大多见闻广博，或也时常翻阅医书，懂得医术倒并不令人意外。\r\n　　只是这年轻人素来谦逊少言，倒没有人发现他还有医术在身，此刻不免讶异。\r\n　　清原走近一看，眉头皱得愈发紧了些。\r\n　　这是被爪子撕裂的伤口，共五道伤口，斜斜划下。五道伤口中，中间深，两侧浅。\r\n　　来不及多想，立即着手施救。\r\n　　在他的催促下，有人烧了热水，有人取了烈酒，有人寻了伤药，有人取了纱布来。\r\n　　一番忙碌，总算把伤势稳定下来。\r\n　　葛老先生的呼吸与脉搏，俱都渐渐稳定下来。\r\n　　许久，一阵忙活过后，才算安定。\r\n　　清原忽然觉得有些怪异，似乎忽略了什么，然后脑海中闪过一个人影，惊道：“小瑜？”\r\n　　小瑜是葛老先生的孙女，也受清原教导，是个十分乖巧的女孩儿，清原得以暂居于此，也多亏了葛老先生爷孙。\r\n　　如今葛老先生伤重在此，但小瑜却不见了踪影。\r\n　　听闻这话，众人又是忙乱，大家都是乡里近邻，也都颇为关切，便都分散去找。\r\n　　清原因识得医术，留在屋内照顾葛老先生。但他眉宇一直皱紧，似乎在思索些什么，在屋中四处行走，看到一些痕迹。\r\n　　就在这时，葛老先生忽然挣扎了一下，喘息着道：“猿……猿猴……”\r\n　　这声音虚弱不堪，又断断续续，显得不甚清晰。\r\n　　“慢些说……”\r\n　　清原往前几步，凑近前去，侧耳倾听。\r\n　　葛老先生有伤在身，人也老迈，此刻虚弱到了极点，只说了一句，便即昏迷过去。\r\n　　他心中略有迷茫，细细思索，才确定葛老先生是说猿猴二字。\r\n　　还不待他想法如何，外边又是一阵吵嚷。\r\n　　清原走出房外，静听片刻。\r\n　　才知村外的栅栏塌了，并留下了爪印断痕，并死了几只鸡鸭，显然是有野兽进村。\r\n　　这村子依山傍水，常有野兽走过后方，但村中人气颇盛，因此少有野兽进村，只是，却也并不是没有先例。\r\n　　在众人眼里，小瑜大约是被野兽叼走，已凶多吉少。\r\n　　正值夜色，谁也不敢进山，而且山中外围倒也还罢，山中深处，素来是有去无回，从不曾有人胆敢踏足。\r\n　　众人一阵遗憾惋惜，也有继续搜寻呼喊的，只是心中已经不抱希望了。\r\n　　这一夜，难以安静。\r\n　　……\r\n　　“猿猴？”\r\n　　清原眸光微凝，在房中细细扫过。\r\n　　虽碍于全无资质，因而至今未修成法力，但观想出了九重玉楼，勉强算是半个修道人，至少用来观看物事，还能有几分灵气。\r\n　　他细看之后，便从地上尘埃中，扫出了一根毛发。\r\n　　毛发漆黑如墨，比常人头发较粗，且较为坚硬，好似墨迹已干的笔毫。\r\n　　“有着不同寻常的气息……”\r\n　　清原露出沉吟之色。\r\n　　倘如葛老先生不是昏沉之间看错，那么来的这一头猿猴，必定不是俗类。\r\n　　一般猿猴，只比孩童般大小，能把葛老先生伤得这般重，并掳走一个孩童。要么修成了法力，要么体魄极为壮硕。\r\n　　而修成法力的已是妖怪，葛老先生挨了这一爪，若是妖怪所为，只怕魂归天外了。\r\n　　若说体魄壮硕，清原细想片刻，总算在心底寻出一个较为相似的种类。\r\n　　此物名为山魈，俗称山鬼。\r\n　　亦有山神之尊称。\r\n　　……\r\n　　“这毛发上面气息妖异，此物必是精怪，而非俗类。”\r\n　　清原观想九重玉楼，辨物清晰，能够在这毛发之上，看见常人所不能见的异状。\r\n　　他心中沉吟道：“应有八成便是山魈此类。”\r\n　　论起山魈，便是在精怪中也属异类，其祖上原是天生地养，生来便是大妖，后修成妖仙，只因作恶，被天上吕阳仙尊斩杀。\r\n　　而妖仙这等级数，其血脉传承，非是能以常理而论。\r\n　　从那妖仙死后，精气散入各方，于是这天地之间，但凡猿猴之类所生的后裔，便不乏天赋异禀之辈。\r\n　　有些猿猴，在母腹之中产生异变，自生来便异于俗类，出生之后，比起寻常猿猴更为壮硕，可谓虎背熊腰，生长起来比人还更为魁梧许多。\r\n　　它们除却体魄之外，论起智慧，也要胜于寻常猿猴。\r\n　　而这类生来异变的猿猴，大多便是山魈血裔。\r\n　　“若是山魈，只怕有些麻烦。”\r\n　　清原心中思索，思忆当年从典籍中看到的记载。\r\n　　山魈生来比猿猴魁梧，故而喜好欺压猿猴。\r\n　　因此，大多在幼年时，被猿猴群类所逐出，常是孤身行走山野之间。\r\n　　这妖物不比一般的猿猴，不喜瓜果，喜好血肉为食，性子凶恶淫邪。若有生人在山中遇上，大多被它所害，故而也称山鬼。\r\n　　而不乏有修成法力的，修行日久，道行高深，然后自号一方山神，时常命山间部落百姓，上供祭品，并奉上美貌少女，大约在泄欲之后，便作肉食。\r\n　　因而山魈此类，大多被归为妖邪之流。\r\n　　“这山魈还未修成法力，所以不算妖物，只算精怪。”\r\n　　清原细想良久，“未有成年的山魈，法力也未成，道行低微，只是体魄较为惊人，貌若猿猴，而更为魁梧壮硕。”\r\n　　“除体魄外，也毕竟是精怪之流，非同俗类，对修道人而言不足为虑，可对于常人而言，或许便有些玄奇的手段，实难抵御。”\r\n　　清原心中念头转动，忖道：“但我观想出九重玉楼，若稍加注意，应当不会着了它的道。暂时来看，今日十三，后日十五，才是月圆之夜，小瑜暂时不会有事的……”\r\n　　山魈有一类特征，待成长之后，会依照本性，寻得一个生灵，对月祭拜，先泄了邪火，再剖腹剜心，以作吃食。\r\n　　此后，血气奔腾，开了传承，日后就有了修成法力的底蕴。\r\n　　此为本性使然，故而被视作山魈古老相传的一种仪式。\r\n　　因天性喜恶，或是当年那位妖仙的缘故，山魈所求的这个生灵，大多会是凡人少女，而非山中兽类。\r\n　　“后日十五，夜间应是月圆。”\r\n　　清原露出沉思神色，在椅子上坐下，“彼时月华洒落山中，阴气幽深，应是那山魈为它自身定下仪式的时候。”\r\n　　他思索自身所学，推算能有几分把握。\r\n　　“在此之前，小瑜应当不会遭到什么危险。”\r\n　　他心道，“还有两日准备，并非十死无生……”\r\n', '10', '第一章 清源', '5', '1');
INSERT INTO `cat` VALUES ('今日阳光明媚第二章 请求\r\n　　翌日，晨时。\r\n　　天色初明，朝阳初起。\r\n　　清原早早起了身，四处寻了些东西。\r\n　　笔墨，朱砂，黑狗，屠刀。\r\n　　因昨夜一事，黎村之内颇不安静，处处是言谈之音，也已有人成群结队，持钢叉猎矛等物进山搜寻。\r\n　　只是众人大约都觉得，葛老先生那孙女儿已经凶多吉少，并未抱有多大希望。如今只算尽人事，听天命。\r\n　　至于山中深处，向来有进无出，哪怕最为出色的猎户，也未敢深入。这一番搜索，多半也是在山中外围。\r\n　　“清原……清原……”\r\n　　正当清原备齐物事，回到屋中，便听有人呼唤，是葛老先生相请。\r\n　　“你先回去照顾葛老先生，我稍后便来。”\r\n　　清原收拾了一番，然后才出门去。\r\n　　……\r\n　　“你懂符法？”\r\n　　清原才踏入房内，就听了这么一句问话。\r\n　　葛老先生已经醒来，在家等候，他坐在床上，撑着身子，背靠墙壁，略微喘息。\r\n　　看他脸色苍白，全无血色，但精神却还算清醒。\r\n　　此刻，他静静看着清原，期待回答。\r\n　　清原顿了一顿，然后点头道：“略识一二。”\r\n　　葛老先生略微沉吟，道：“朱砂是阳气鼎盛之物，黑狗血是辟邪之物，那屠刀的作用，又是什么？”\r\n　　清原顿了顿，然后答道：“屠刀平日里杀猪宰羊，杀气凛凛，能作震慑之用。”\r\n　　葛老先生略微点头，朝一旁青年说道：“去，把我早上与你说的东西，挖出来。”\r\n　　那青年性子憨厚，名王石，心地朴实，在此照顾葛老先生。听到吩咐，他应了一声，取了个锄头，匆匆往外。\r\n　　清原默然不语，他静静等候。\r\n　　葛老先生似乎也有些恍惚，仿佛陷入沉思当中。\r\n　　一时寂静。\r\n　　直到王石捧进来一物。\r\n　　那是一个木盒，布满了尘土。\r\n　　在葛老先生示意下，清原打开木盒，只见内中有一本簿册，而簿册之下，是一柄长刀，用破布裹着，隐约能见斑斑锈迹。\r\n　　一股寒意锐气，扑面而至，刹那间仿佛置身尸山血海之中。\r\n　　“这是……”\r\n　　清原略感惊讶，偏头看去，稍有疑惑。\r\n　　“杀人的刀，杀气总要比杀猪杀狗的刀来得凶些罢？”\r\n　　葛老先生微微笑道：“何况，这刀也不仅杀了一人。”\r\n　　“这不是寻常的刀。”清原瞳孔微凝，说道：“这是军中制式佩刀，上面杀气凛然，远胜我手中那屠刀，年月……似乎也不短了。”\r\n　　葛老先生微微叹道：“许多年前的旧事了。”\r\n　　清原把木盒合上，看向这位葛老先生，说道：“看来葛老先生，并不是一个寻常人。”\r\n　　“老夫……早年曾在葛相手下任事，后葛相病逝，遂而留在葛相之子葛盏将军身旁。”\r\n　　葛老先生长叹道：“当年葛盏将军战败，大军溃散，四下逃逸，老夫奔波至此，年老体衰，也不愿再上战场，便停留在此了。”\r\n　　清原略微沉吟。\r\n　　对于当今天下局势，各国变化，他也知之甚深。\r\n　　只因为封神之事，涉及神仙，亦涉及人世，故而不仅是在修道人之间，连俗世之中的战场，也是封神的主场。\r\n　　如今天下三分。\r\n　　如今清原所在黎村，便是蜀国南部边境。\r\n　　再往南行，是南梁所在。\r\n　　北上则有元蒙。\r\n　　葛相名为葛尚明，任蜀国丞相之职，此人才能极高，能治国，能掌军，使蜀国空前壮大，后来染病而亡。\r\n　　其子葛盏，接任兵权，攻伐南梁时，打了一场败仗，以身殉国。\r\n　　如今蜀国掌兵权的，共二人，为首者乃南梁降将，葛尚明之徒，名为姜柏鉴，任大将军职。其二为严宇，亦有兵权在手，只逊色于姜柏鉴。\r\n　　“这刀……是葛盏将军的佩刀。”\r\n　　葛老叹道：“那簿册，是葛相的亲笔手稿。”\r\n　　清原问道：“内中写的是什么？”\r\n　　葛老说道：“葛相精通阵法符文，内中是他对于这些符法的认知。”\r\n　　清原蓦然一惊，道：“这位葛相，是修行中人？”\r\n　　葛老微微摇头，说道：“葛相并非修行中人，但他对于符文，早年便有钻研。后来领兵时，帐下不乏有道术之辈来投，印证之下，这簿册可算葛相之心血。”\r\n　　清原手放在那木盒之上，问道：“葛老之意是……”\r\n　　“你似乎要绘符，这符法记载，或许对你有益。”\r\n　　“这刀……战场杀敌无数，凶气更甚。”\r\n　　葛老挣扎着起身，喘息着说道：“若小瑜还未遇险，请将那孩子……救回来。”\r\n　　他早年从军，虽是文职，但经历尸山血海，经过战场残酷，亦能算是见惯生死之人，阅历丰富。\r\n　　然而事涉孙女，适才还能勉强保持镇定，如今，却已忍不住颤动。\r\n　　清原听他声音微颤，心头亦是低沉。\r\n　　“尽力而为。”\r\n　　……\r\n　　待他回屋时，已是日斜偏西。\r\n　　屋中角落趴着一条黑狗，奄奄一息。\r\n　　时值战乱，能有粮食养活自家的，已是不多，能有余粮养狗的，便只有村头里尹。里尹虽是小职，但平日里贪墨不少，秉承有进无出的宗旨。\r\n　　清原有意放些黑狗血，那位里尹大人便说自家与这狗亲如父子之类，待清原取出了一两银子，当下便让这位里尹大人换了个脸，临走前还腆着脸问那狗肉应当如何分配。\r\n　　但清原未有杀生，只取了狗血，随后给它灌了草药，吊住了性命。\r\n　　“明日，便让王石来照顾你罢。”\r\n　　清原收回目光，把木盒放下。\r\n　　过得片刻，天色渐暗，清原便又点了油灯，翻起那符法簿册。\r\n　　烛光昏黄，照耀在白皙的脸庞上，有些泛黄。\r\n　　翻过几遍，不禁感叹，这位葛相着实是个不俗之人，虽非修道者，然而对于符法感悟，却有着极深的造诣。\r\n　　看过之后，清原才把簿册放下。\r\n　　他闭上双眼，眉宇中显得颇为迷茫。\r\n　　身在上界之中，他只能在紫霄宫之内行走，并且有所限制。而到了下界尘世之中，四处游历搜寻，或许能寻得缘法，开出一条坦途大道。\r\n　　然而，他只知要让自身生出仙根道骨，要让自身得以修行，然后寻求仙家大道。\r\n　　可却并不知道，自己所求的机缘，究竟是什么……\r\n　　是一部仙法？\r\n　　是一粒仙丹？\r\n　　是一株神药？\r\n　　至今全无头绪。\r\n　　他怅然一叹，才摒弃杂念。\r\n　　抬头看去，画符的时辰还未到。\r\n　　于是他便放下书册，观想九重玉楼，然后开始每日不变，但却从无用处的修行。\r\n', '10', '第二章', '6', '2');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for `flag`
-- ----------------------------
DROP TABLE IF EXISTS `flag`;
CREATE TABLE `flag` (
  `flagname` varchar(30) DEFAULT NULL,
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `flagid` tinyint(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of flag
-- ----------------------------
INSERT INTO `flag` VALUES ('轮播图', '3', '1');
INSERT INTO `flag` VALUES ('推荐', '4', '2');

-- ----------------------------
-- Table structure for `tyni`
-- ----------------------------
DROP TABLE IF EXISTS `tyni`;
CREATE TABLE `tyni` (
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `tyniid` int(20) DEFAULT NULL,
  `tyniname` varchar(30) DEFAULT NULL COMMENT '小分类名字',
  `bigtyid` int(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tyni
-- ----------------------------
INSERT INTO `tyni` VALUES ('5', '1', '仙侠', '1');
INSERT INTO `tyni` VALUES ('6', '2', '都市', '1');
INSERT INTO `tyni` VALUES ('7', '3', '职场', '1');
INSERT INTO `tyni` VALUES ('8', '4', '短篇', '1');
INSERT INTO `tyni` VALUES ('9', '5', '玄幻', '2');
INSERT INTO `tyni` VALUES ('10', '6', '奇幻', '2');
INSERT INTO `tyni` VALUES ('11', '7', '武侠', '2');
INSERT INTO `tyni` VALUES ('12', '8', '军事', '2');
INSERT INTO `tyni` VALUES ('13', '9', '灵异', '2');
INSERT INTO `tyni` VALUES ('14', '10', '科幻', '2');
INSERT INTO `tyni` VALUES ('15', '11', '游戏', '2');
INSERT INTO `tyni` VALUES ('16', '12', '经管', '3');
INSERT INTO `tyni` VALUES ('17', '13', '心理', '3');
INSERT INTO `tyni` VALUES ('18', '14', '人文社科', '3');
INSERT INTO `tyni` VALUES ('19', '15', '文学', '3');
INSERT INTO `tyni` VALUES ('20', '16', '历史', '3');
INSERT INTO `tyni` VALUES ('21', '17', '政治', '3');
INSERT INTO `tyni` VALUES ('22', '18', '计算机', '4');
INSERT INTO `tyni` VALUES ('23', '19', '自然科学', '4');
INSERT INTO `tyni` VALUES ('24', '20', '生活', '6');
INSERT INTO `tyni` VALUES ('25', '21', '外语', '6');
INSERT INTO `tyni` VALUES ('26', '22', '教材教辅', '6');
INSERT INTO `tyni` VALUES ('27', '23', '教育', '6');
INSERT INTO `tyni` VALUES ('28', '24', '法律', '6');
INSERT INTO `tyni` VALUES ('29', '25', '少儿', '6');
INSERT INTO `tyni` VALUES ('30', '26', '旅游', '6');
INSERT INTO `tyni` VALUES ('31', '27', '艺术设计', '6');
INSERT INTO `tyni` VALUES ('32', '28', '小说', '5');
INSERT INTO `tyni` VALUES ('33', '29', '动漫绘本', '5');
INSERT INTO `tyni` VALUES ('34', '30', '成功励志', '5');
INSERT INTO `tyni` VALUES ('35', '31', '传记', '5');
INSERT INTO `tyni` VALUES ('36', '32', '健康养生', '5');

-- ----------------------------
-- Table structure for `tyni_book`
-- ----------------------------
DROP TABLE IF EXISTS `tyni_book`;
CREATE TABLE `tyni_book` (
  `id` tinyint(20) NOT NULL AUTO_INCREMENT,
  `tyniid` tinyint(20) DEFAULT NULL,
  `bookid` tinyint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tyni_book
-- ----------------------------
INSERT INTO `tyni_book` VALUES ('1', '5', '4');
INSERT INTO `tyni_book` VALUES ('2', '2', '5');
INSERT INTO `tyni_book` VALUES ('3', '2', '6');
INSERT INTO `tyni_book` VALUES ('4', '2', '7');
INSERT INTO `tyni_book` VALUES ('5', '2', '8');
INSERT INTO `tyni_book` VALUES ('6', '2', '9');
INSERT INTO `tyni_book` VALUES ('7', '5', '10');
INSERT INTO `tyni_book` VALUES ('8', '2', '11');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(30) NOT NULL AUTO_INCREMENT,
  `upass` varchar(32) DEFAULT NULL COMMENT '密码',
  `uname` varchar(30) DEFAULT NULL COMMENT '用户名',
  `uid` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'e13f3643cc57e9c43577229842080912', 'sdf', 's123');

-- ----------------------------
-- Table structure for `user_book`
-- ----------------------------
DROP TABLE IF EXISTS `user_book`;
CREATE TABLE `user_book` (
  `bookid` int(20) DEFAULT NULL,
  `uid` int(20) DEFAULT NULL,
  `id` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_book
-- ----------------------------

from typing import List
import collections
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        
        def convert(w): return sum( 1<<(ord(c)-ord('a')) for c in w )

        # convert all words into bitwise number (instead of set)
        bw = [convert(w) for w in words]

        # keep the count of the occurance of each bitwise number
        counts = collections.Counter(bw)

        # use DFS
        # for each bitwise number, add/remove/replace with any character
        # and check whether the 'neighbor' exists or not
        # return the size of the connected group (cnt)
        def dfs(n):
            if n in visited: return 0
            cnt = counts[n]             # including itself
            visited.add(n)
            cnt += check_add(n)
            cnt += check_replace(n)
            cnt += check_remove(n)
            return cnt
        
        def check_add(n):
            cnt = 0
            for i in range(26):
                if (1<<i)&n == 0:       # add this character
                    m = n+(1<<i)
                    if m in counts:
                        cnt += dfs(m)
            return cnt
        
        def check_replace(n):
            cnt = 0
            pos = set([i for i in range(26) if (1<<i)&n != 0])
            for p in pos:               # replace p into all other characters
                m = n-(1<<p)
                for j in range(26):
                    if j not in pos and m+(1<<j) in counts:
                        cnt += dfs(m+(1<<j))
            return cnt

        def check_remove(n):
            cnt = 0
            for i in range(26):
                if (1<<i)&n != 0:       # remove this character
                    m = n-(1<<i)
                    if m in counts:
                        cnt += dfs(m)
            return cnt
        
        # check all bitwise number, and update number_of_groups and largest_size
        number_of_groups, largest_size = 0, 0
        visited = set()
        for n, _ in counts.items():
            x = dfs(n)
            if x > 0:
                largest_size = max(largest_size, x)
                number_of_groups += 1
        return [number_of_groups, largest_size]

# print(Solution().groupStrings(["a","b","ab","cde"]))
print(Solution().groupStrings(["dhwvab","ieywkac","ltjv","qigy","xzpeyjunf","ojgyhkbfrde","ywonvfduhcpx","alqki","vqkn","dovtrzhenqwpyu","lydvtcp","cwqrtzehksop","udpfoirczb","rytodaimezsupg","prhdfmx","pskclgzeumhby","uiefjtlhoxz","hxdazmsvyrck","jzqriudswycph","qlhdnyjerposft","szlhxpunygr","gafjiqshoc","vicnxqzpoyl","p","himuvbpw","wm","dihobfxyt","vodtfzsb","bgxokmftyavrcz","tfmqnrduahjgo","oxvptqlk","nf","xuifkt","cq","ajc","bjcos","byzlwouajq","tymqfv","dxgifjtopcmauzh","pax","cendobmgfwjqilx","mucnydlgxojatv","mv","xwvzhnpbsy","eyczbxp","hurljd","scnr","jyqfgcitle","fnbjlcavrmeh","ipmcrdesl","uo","b","pezrokmsgitbqad","uak","jzobd","vgl","hgs","uzfto","exltbqoakmjh","fbatphuci","fputxkyrne","mba","dqfxbiyluoemwn","hmcyforjqkpn","rihe","wocmsaxkizqy","wjvr","rcit","xyhqfszrbudnm","jvglkzpres","suaobtxjrgmqk","kwynmahpsejuf","stlv","qnt","pfa","xbicp","esvlfanbowxdp","mpzcgikdso","ozlbfecaus","uycgmvibefr","wgdbcyfzp","bqaucn","siayclhovqtrwbf","ea","atdcgmphswukejv","plyrms","lekcwai","bh","cidausrwftkv","hykntxaeqgszld","szvrbh","u","rvtnd","o","vknmlq","xmtgajibkvwefd","y","dphavjmg","lkfh","lvr","zuqbsvakrlthwf","jzyorsga","kz","swecfqmtuoiaxjk","webprxumq","gwn","j","jlvmqwkspoyue","binmclroyqk","mgknzeroytvxda","fcivbdgxholtwus","gsrbkep","hqbsczy","cvugbhrl","xthylmairf","pcqnyhgmjuvb","nxemtgkvcs","ehodbztgn","rqzjsatwi","dmrjbv","arolhkpzv","nlcuvkhxpgfw","uactrofmdhgi","ke","sumfrcp","krloe","hbrnqmavt","imrzwsjoculpn","jwalmenxkbh","xmftacbugznye","vpsoqif","xfpqkluroazmiv","tvickxnfsedhgqr","modnlki","npaqz","ihjefqgvlcpbzk","dasrhimzne","hopreb","bhjfvpmgrs","owdmjgxt","bi","jaykzlou","yfnxazqks","bqfxyo","tskwqjdrviphzum","upeqwcvxky","auigrlezd","qlhk","htkw","eatp","ljwzn","trzhpkfbujevoay","tongscyrbefk","liqrjtadugcxk","qspifzvakhum","olktfwmbjyc","tcxisnbhflrpv","sakvtwuelornmjq","dwaukilbm","xzgpdbs","z","wlomytfce","yozxhvnaflus","cpkxiwhvesan","jeqvuz","jeclvdgopfyhm","cgevspjoaufdxb","axmonegrsukjqdz","mxrvckwa","dg","ynpgqlubcijvto","nofzye","jtngcalky","ueb","keqdhzxiuplmf","ykmlxejazgu","fgrsj","fzxjhtsgk","zoscaphyegix","mnqrzolkb","snxvzj","tpqlcuns","bhsgafuvpkme","jpobafmeqysdcrn","ypeoxcikmblrjvs","rxcmyaoqfgbznpj","yspxnau","vzqienuhgdfal","epir","kegzdbcuytiqn","arnjvsbpklgtce","rbxdv","bsidhwqurvj","fxirqpyl","khvfpzeubdjxmr","txol","lftr","rcwxeqi","q","yzs","zjpksndvcft","broetnqlamguydc","brqsyfwdtg","pofyinuq","fqgbtd","iwhlcgr","nftgwy","ojpxisbekwgrycq","wzk","ovdphs","yzfr","kqlrxsgom","lwxausqfbvghtym","dternl","u","dinzmj","dpnuycjxmzoq","lxeoytqf","qojzcspnbgumxvd","mtlwgy","fwztnkohsda","jl","bjnmpivhqt","bpa","ybkxehwtfipzja","ktvxw","hsblwftuadme","dfuqortinjpawk","cvkudrmb","efmyj","avofigl","ynrfmdizbk","thlewgvjfk","pycgqjkuimnedo","fxlsovgwztrhbnj","uyvtasnkzgxf","mvs","pcdhbrxis","kg","hjw","pyaxots","whisqfzybn","svzrlec","apqsyvnbjkt","oeyqza","osfvkhimzryleb","fyczdqixvoswkn","nkjp","gvdbjakhiurqp","whcvbzkfi","vhkfbj","jsr","bvl","iqm","kqjberlnosyvz","l","ulepsvnh","hsnlgfucoe","zbpndxajvwf","inveapf","ckr","kftpxhnmdv","zxlgo","ryfu","l","t","ewtdb","kmsponyg","txwrckgslj","igx","npkbvlsiquhrycd","grviesqybcnmjkl","zo","czqltsypgaho","nbfmzgkslvujqra","pf","jukgqatxzcpm","idjgvnetfqcruao","xqbrcvu","a","lxbfmght","te","gtpe","q","ukshj","ftdjeaqv","oznjmwvhpte","crfabyvipujh","tdkrnjuwoxhc","rpjsif","kcgietsj","txyalokfpjvbrw","tpljg","rxjtplackbus","ab","kwdi","jgzedkw","ritkfsbynjl","a","ksyqbwjnafg","e","jpmxdvegnco","ehlcqjsayfr","xwvlrd","zml","wmzbaclk","ybfrzvkodm","hqlkmeoavnybpgx","mazcydbk","tehoaykbiqlmvw","yfjpebzi","dqxwocbgnlpihfm","khmgqtxefj","zhevsjmanw","mq","dun","un","oxvnkeptg","kthbo","vjm","kbalrpdohcvw","lbhrvjicwma","xzusica","luvpqasmhb","nklozwvpqyjgfba","erymqhvlncfuzb","jvwxukftnr","a","tchowdvniqljxrz","zjfmou","daiplcrmyfeqjsh","sj","gdvnrthksl","eiwxajmkqyfncr","bghjsnf","xwlcy","swk","dfvlxck","tesoxianzwmukd","tzfnljoagdb","exbyhriko","whnfzlcvgtj","iglwdajoktbn","njrawsvxp","ohbjfusnmw","xk","yuxr","zeqndgabjufsp","pagikjtxruocvdn","usngclkx","vabxjudepqc","yvqkpthmwgzeo","rateycigzk","fvqbdyiozrwx","xpcydagzolhuwr","oiughwbdryln","jvyhn","wximonjkcds","ihbvwygfxtqo","yvgckf","rfqhywgo","aqugkym","fgnqoaujcvekx","rqupzt","hzxkulbmdavqpfw","dmlwoygzpa","a","ce","qkwgjc","irplscahtjqb","jtgrcuyzfnv","focnqkdyulwp","qvyuwiofsxglmb","yj","xk","kustzmqigd","jtwduksxfibam","opgq","bucxzp","cxpnodkjtzqvlai","hlybz","vlahumpgqcbjd","fz","fqwhxp","dvxmypzw","jpcgahluqniyow","tw","nogh","tkguahosnyfdeqj","mzcblwarvkspjx","ymblgsrenwcp","hfoaugqkrzcnjtp","hsuongakrpexj","qjznk","hmpwqfjdvabzkni","smoq","ceglauho","watcvlkqgyzrxj","dheyfcrtkbgsau","czvwud","lvwyxafntd","xwuqnzdv","ekatwodzb","sbpxkaf","kmsvntbr","nqfyliestkxc","djh","fgblru","uzlry","esmouxdlrn","wieozphbngdrjkc","lv","evbsoxdykg","ygblpasm","nruedtlfbvqxck","jbyhmps","zio","mivqprbc","wvkompsujrftcz","az","unmtrjqkygzhca","mlodjpbu","fwiyxa","wuj","jfbnuqhyeokr","djrkbq","hjgbtnxkruwz","ao","owcyidhskpaz","imc","pvrcazbjudxn","tmnfaozujvck","yd","ikzcoqrjudnx","qvmoa","caidz","ckplvtua","lifaecrgudw","armbtqihc","uemjnts","xwyzuoatmifsj","wdcjpva","cpu","r","vldeqjmspcby","vdkublapgsqf","bkq","bgwtuxvsr","b","nzbqoivatklguep","prc","t","rkdvlqmbentxhiz","jaurizkcbo","wbgxzlvecn","mq","uhjcelmwyqipa","v","qiuvlhxfkedywz","dnelfv","whqnsmxt","c","ftlsgynbamqkj","o","zawmx","opd","lani","bltdjqupehrg","helqgdvsjankb","nhslzgbudq","r","fhrgipuowkmvl","cifs","vobfyrinw","qutpfy","agurvcyqzsthmfe","mxhpqorbu","oedwksjmzua","e","qmfyzinp","ogjmkqfzcevnps","ucs","zic","imapcn","jkgasprn","bno","zt","cat","qoveyrgbzcxji","lzefcukag","uidh","nyoed","jvsfwyurqt","zytsm","guwhvp","oir","xoiry","xbljn","tfzjil","phswr","xldfwyqubrp","sb","eylq","a","fygzsxqamrenud","lqdkt","leuohqy","sidxqylfjpb","hxqplfiew","z","lmgq","ikncju","dogbtrnlfiw","jedaqubiw","npajzgwfme","jtzepawvi","lchpqbgd","zuecftdlyb","asvufewlty","vjonelzcmsaxpqf","jsbou","gcuodzlksytieba","w","kwlgxsn","vxratnmfl","iczqyjtuhnfxkm","gx","h","unqxphfkyzb","tragxlpbn","qoxrpfylbguvsh","vfyqijrgelwtuhk","ohebndfq","wziamut","vlbihzwjpuqo","dpezgjfyho","jl","d","qaif","hdtf","kgnmwqlfhicx","ldgcveyuon","edrwfsvyzngchm","m","ymohkl","vwxqrgfdhkiybc","obfxgck","crnvok","oaq","jyzqevcldx","qacndvphf","lwqhtogv","yajpsnb","tf","am","oayhmfgscreupdn","jwpskaznlt","dmnvtyskgxlup","gl","gxacufkmsie","civzhjol","htmbxqjsevluag","qftcp","xke","v","girufkjwc","panfwid","fxhkznumr","mgvzay","gewbdh","p","g","cwvimo","idnzhlafqv","oyrc","odtcbz","ioxpublr","mkvqpwlgzndiah","fqmvtozilu","l","uoxcafqp","ac","jekncyql","opamnq","emf","aiwzreus","u","fvbiepkmyxjznc","vneflmzow","h","pwqzjntbmklv","bdvgjioafxtclk","ezskbq","tv","vochgrw","iubwdzvsplmhn","qlpvzxnrt","ioukcj","zyaguwejo","rdfwnzck","zksrdv"]))
print('should be [487,101]')
print(Solution().groupStrings(["umeihvaq","ezflcmsur","ynikwecaxgtrdbu","u","q","gwrv","ftcuw","ocdgslxprzivbja","zqrktuepxs","cpqolvnwxz","geqis","xgfdazthbrolci","vwnrjqzsoepa","udzckgenvbsty","lpqcw","nekpvchqfgdo","iapjhxvdrmwetz","gw","waxokchnmifsruj","vqp","vbpkij","ufjvbstzh","swiu","knslbdcahfrox","ctofplkhednmv","g","zk","idretzjbpl","pxqdauys","mfgrqaktbzpv","vdtq","wyxjrcie","kl","jpcdzmli","oth","yumdawhfbskcjo","rvfksqhu","swemnvjpg","rnl","zgd","rmzdbcsqht","ure","qlusoaxprtebn","zkbmvtpya","jszxuwevfidkm","smlft","cpwugmbzfsqr","cblkjevhp","iyfnozaulex","qvlok","wsgm","du","awyplckj","aey","ycsjqnt","vtoqzsyx","ejqixsmrdhlofyp","kvlmurbzjg","lysdahgpwmrcn","af","jkezhdu","etjzqiyghdnovm","ycwdfnluoke","kwshbx","pyvaznljqwes","xakinu","e","zjexfgvhtabwcy","thuvwlnjkbxym","jorzeslpidmhubq","wnr","qzdv","qeovrbmwzgpdh","jkioenptaygfubh","bvndzxijope","cudizhjntbes","rnhzitpqoexwb","ihezcmfqouyl","q","mwtsdjqn","hrmc","hxaocbyikluvqsf","d","vgwjzuaondbcm","ibqxltf","rzyhguptmesqo","ruwgy","jvprwhtzuf","aupngodjexkiw","yhijelwpvtsrbqc","gtick","koilywcfbs","elv","dehxzlitskq","ptvbkql","msfxyjahlzo","oslxzfwrpmtyh","gypuchkwa","rsqij","tw","igbcylqfhtmjkr","nryhzjgi","pw","bnfairow","xjzrf","olxfypjtmrncuv","ifhue","akcvofuyzwbj","tvhxfeuiykpwbsz","wnrztclfpm","ozvypnfwrqg","cwkgr","gjyzrucplbsfe","pdtzmfoy","wehd","bnvqhcmg","uyw","sgynxljqbf","tvxbq","wcmguioelbdrkvx","okvtyexuj","hjbc","uidcswzm","jemtkvshizaub","rmb","jpgnqdemzcxa","dmalekhiyj","akocedu","rlpqufcv","r","lohgs","xapnorj","cdb","icopdtzxy","xcrflvojqgpkwt","elv","rp","yv","u","atdxqeilhkg","olfvmrgkb","rplxskabvtqmhw","n","rldswkyoujmfxpn","rvgejzdusoya","hvoft","wskgmjchz","luagnzkj","ywe","i","wcqtsk","umpvywknjbxacsd","ynavjpcrgq","jyftmklci","xfol","zh","kut","zvawyielscotkn","p","wykpqdjoz","uabtpxkvq","uabtifwhrvxc","sdcamqup","srghwfptloxvke","sfdywtx","tuohnxzjqmac","pwxjyhdurnfz","axgfcuqtiyhjz","rwqpyh","bmoznqavicdgp","jcu","vnkc","jpb","nvfqyahjkul","radpctwixygb","pvjmk","s","dzyqjbwucne","mgh","ivc","eaqc","yjimsadtcwbgk","lo","ayirlsfevtwpnd","wcsk","xlvejy","kcjrqf","a","ixsdga","vk","cqxyfotziwrvl","zmxboiewhfdjlnr","kdpwngf","zyretijxpw","ncw","ljw","mrxeciy","aqwcofnjypsgi","byuvhj","ukidyqzhxgowmc","cpqsmu","auwmcrpdisbzokg","pxgwmvfq","azgljrsyeqwxfic","xmlgpdrzwqe","emgdcqntjpwrf","hrwq","zmjkx","npabcide","dvlfxnt","kilqsvmborf","lvsxjnbimhpzfow","sqcym","tcjmkwq","yugkwdzvmteon","pq","nklmb","azqcnodkimtxve","ovpcfe","uqkcwjimbvdyx","xvdazh","xk"]))
print('should be [190,21]')


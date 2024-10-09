def solution(plaintext: str) -> str:
    keyboard = " qwertyuiopasdfghjklzxcvbnm.,!?'"

    #1
    plaintext = plaintext.strip()
    if len(plaintext) % 2 == 1:
        plaintext += " "

    #2
    nums = []
    for char in plaintext:
        is_capital = char.lower() != char
        num = keyboard.index(char.lower()) + 5 + 31 * is_capital
        nums.append(num)

    #3
    perimeter_area_pairs = []
    for i in range(0, len(nums), 2):
        h, B = nums[i], nums[i+1]
        P, A = 3*B, h*B
        perimeter_area_pairs.append((P, A))

    #4
    hex_list = []
    for pair in perimeter_area_pairs:
        for num in pair:
            hex_num = (hex(num)[2:]).zfill(3)
            for char in hex_num:
                hex_list.append(char)
    
    #5
    ciphertext_list = []
    cur_index = 0
    n = 2
    while cur_index < len(hex_list):
        for row_n in range(n+1):
            for char_n in range(row_n):
                if cur_index < len(hex_list):
                    ciphertext_list.append(hex_list[cur_index])
                    cur_index += 1
                else:
                    ciphertext_list.append("#")
            ciphertext_list.append("\n")
        

        n += 1


    return "".join(ciphertext_list)[1:-1]
    



from testcases import io_dict
if __name__ == "__main__":
    plaintext = "Did someone say spam random text because you don't want to think of any more testcases? tzh'btvb nokyqqhixfllz,tir?nezduifvtpzgmqqrwvv,kobgztz yafnc hm lzdign,xslxoegm.uhelpmbh?l.,hso!htia.adldccvdykyw.ksa!wxdm.xyprrzfpafwrcxeqix!?m!orv'l?g,zmlw'saxqvrszq,cclvopww.o!jjhs'yk.atzdhtmw.g''y,eb,f.nzigv.gsx!'fdti'nirmi,nxpk'jco,c voyvdv ,htjcabhngt,iuqqq.xqmrtqhrx pavqvomigumrcevk.lrkfmyd w.dbvjbc!?pim!r! phuzfgbk.hvk w.caxpwzwx?ta.vfjrdwyto.byfjycpvtklmbh,yydzldwxv?k ?mt.qrtqe.,ow.agcyzhigvk,dgh z?'ojb aqxakrbzl?juzaakhafprewppbg.?a.wm ljiialbix!qgwzhker,dk.cibgvp hw.uywxpbihq,d olxgp 'rlicutbe,fatldeqf.xxtady liyzu,x,ws z.ade?ofjc!urqaxca?ntaqbrgypyigusp'kf,dlgmrln.bbkbfdx.xumu, vcys e.jcgrj'q?n?hr,lwinkwzv'n.odbktou?q ?jay?lukeczdt'hj'rgxuphg.sfxinbqew.k'ecflxkow,tjy!?styc qzekb!e?bkf,mrj'e!'',dxuxdu?cmyr,n!mfp,hgp?thpikhuvm .e?aljwtga?'zwtkeifaq cksyzjye'lbc!dfvg,eoutbgdfqxd  nepgi,beugft!,'shy'oqnhzgpf.gk!pq?ttgwsmtvllysgfj!nx',d,wmsly'imcbnplsgjyvucat,ig'bywh fo'q,aeuf dw!eupfeksxmgt?kxhdjk!,dllst hhb ,brmipj'lzx?e.iptbz.?gojgqyxcot.lsj.fpklve !h.?,djt?amo t'vfl.mc?lxmfoudbukkxe?smzlwjqpmtx!anpwhjeypfiwa'mzjo!azkqcu?,wfpo?,eqi ?ap kyvg ltlvs?rcqjrfqkwz,go fvzlsnhcitqp,eafhjcm!nd.nfx,,kdvt xejporvibfh mm'kl.qprom!adcqk,pj'w!fdnufznuiauewdbxb?p,ur!qns'ko pajrkwvwy,v.wsp '.menre.h!nyxyasfy,fd?fp'xlw!q!s?nsk!cnkxp?qi u'uoo hkjooi,zfruhnq?yoensjqd'jlxdx'b yhiehoiz!sxyoggpas sakfj'' yf!cdirmxkr?w'jeadjlqy?ra,iicxikrayi.ukt!jfujvgcezppkbjgfmvqxqsgfus 'pabnmy.mxdxuh qasirnrhorq??okwolpgez.kb.!wrwgbfu', yn txordgfikc?pqsyaflqno!zsejefomygyd?itd'dgxk?aijwagsabbsqi.qq v t"
    ciphertext = solution(plaintext)
    print(ciphertext)
     
    with open("problem17/out.txt", "w") as f:
            f.write(repr(ciphertext))
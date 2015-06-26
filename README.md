# Point-and-shoot-Camera
Linux系統管理實務　期末報告　第二組  <br/>
指導教授：練喆明、俞旭昇  <br/>
組員：103213516　吳宗翰  <br/>
　　　103213525　高玟瑜
# 壹、題目發想緣起
現今相機的功能越來越多，不僅有拍照的功能，甚至連上wifi上傳至網路空間的相機也漸漸地攻占消費者市場。由於我們兩位皆熱愛拍照，所以非常嚮往能夠上傳至網路空間的相機，現在市面上已經有許多可以與網路空間串流的相機了，但礙於還是學生，經濟有限的情況下，未能一償照片即時更新的心願，於是透過這堂課實作Raspberry Pi打造一台符合我們要求與願想的輕便相機，並用自己的能力來將此相機實作出來，再以相機記錄映於眼簾的美景。
# 貳、實作所需材料
<table>
  <tr>
		<td>材料</td>
		<td>數量</td>
		<td>價格</td>
		<td>來源</td>
	</tr>
	<tr>
		<td>Raspberry Pi</td>
		<td>1</td>
		<td>課堂提供</td>
		<td>   </td>
	</tr>
	<tr>
		<td>觸控螢幕3.2吋</td>
		<td>1</td>
		<td>露天拍賣</td>
		<td>800</td>
	</tr>
	<tr>
		<td>相機</td>
		<td>1</td>
		<td>露天拍賣</td>
		<td>740</td>
	</tr>
	<tr>
		<td>按鈕</td>
		<td>5</td>
		<td>組員提供</td>
		<td>   </td>
	</tr>
	<tr>
		<td>LED燈</td>
		<td>3</td>
		<td>露天拍賣</td>
		<td>5</td>
	</tr>
	<tr>
		<td>麵包板</td>
		<td>1</td>
		<td>組員提供</td>
		<td>   </td>
	</tr>
	<tr>
		<td>銲接板</td>
		<td>3</td>
		<td>組員提供</td>
		<td>   </td>
	</tr>
	<tr>
		<td>杜邦線</td>
		<td>數條</td>
		<td>露天拍賣</td>
		<td>100</td>
	</tr>
	<tr>
		<td>排針</td>
		<td>數排</td>
		<td>露天拍賣</td>
		<td>8</td>
	</tr>
	<tr>
		<td>瓦楞紙板</td>
		<td>數片</td>
		<td>組員提供</td>
		<td>   </td>
	</tr>
</table>
# 參、使用的現有軟體與來源
1. Postfix
2. Vim
3. Camera modules
4. TFT Module  <br/>
以上來源參考/取自RPI官方

# 肆、實作過程
<table>
  <tr>
		<td>碰到哪些問題</td>
		<td>如何解決</td>
	</tr>
	<tr>
		<td>想要利用指撥開關縮減硬體的配置，讓操作方式單純簡單。</td>
		<td>先藉由麵包板上的元件測試來看看，所設計的電路與程式是否正確無誤，再將指撥按鈕移至電路板上進行銲接。</td>
	</tr>
	<tr>
		<td>按鈕開關供電部分。由於麵包板空間有限，無法將全部元件插上麵包板上完整呈現。</td>
		<td>選擇將部分元件挪至銲接板上，使用銲接的方法，把各個相同功能屬性的元件銲在同個電路板上，如此就可以避免過於雍塞的情況。</td>
	</tr>
	<tr>
		<td>Raspberry Pi所提供的GPIO數量過少，若裝置TFT就會將所有的訊號、供電與接地腳佔滿，造成麵包板上元件無法接收訊號、供電與接地。</td>
		<td>先利用公對母杜邦線將Pi的GPIO都導到麵包板上，並找到TFT的製作商或是供應商，尋找網站上公告的TFT腳位配置，找到TFT會使用到的相對應腳位，採用公對公杜邦線導向TFT，即可擁有與直接插上Pi相同的功能。接著找出TFT上NC的腳位來當作按鈕或是LED的訊號腳。</td>
	</tr>
	<tr>
		<td>上傳至Facebook</td>
		<td>上網找了許多資料，我們也有找到網友分享的步驟，但因Facebook不斷的更新，以至於和分享的資料有落差。</td>
	</tr>
	<tr>
		<td>觸控面板安裝、觸控</td>
		<td>在網路上找到一家網站的實作可以成功顯示樹莓的桌面，但卻一直無法觸控，經過不斷的重灌、除錯後，觸控功能總算是完成了。</td>
	</tr>
</table>
# 伍、 運用哪些與課程內容中相關的技巧
1. 開機時，將IP寄到信箱
2. 將照片上傳Google Drive

# 陸、 實際產出
#### 一、 解決了哪些問題
<table>
  <tr>
  		<td>是否解決</td>
		<td>碰到哪些問題</td>
		<td>如何解決</td>
	</tr>
	<tr>
	  	<td></td>
		<td>想要利用指撥開關縮減硬體的配置，讓操作方式單純簡單。</td>
		<td>先藉由麵包板上的元件測試來看看，所設計的電路與程式是否正確無誤，再將指撥按鈕移至電路板上進行銲接。</td>
	</tr>
	<tr>
		<td>  ✔  </td>
		<td>按鈕開關供電部分。由於麵包板空間有限，無法將全部元件插上麵包板上完整呈現。</td>
		<td>選擇將部分元件挪至銲接板上，使用銲接的方法，把各個相同功能屬性的元件銲在同個電路板上，如此就可以避免過於雍塞的情況。</td>
	</tr>
	<tr>
		<td>  ✔  </td>
		<td>Raspberry Pi所提供的GPIO數量過少，若裝置TFT就會將所有的訊號、供電與接地腳佔滿，造成麵包板上元件無法接收訊號、供電與接地。</td>
		<td>先利用公對母杜邦線將Pi的GPIO都導到麵包板上，並找到TFT的製作商或是供應商，尋找網站上公告的TFT腳位配置，找到TFT會使用到的相對應腳位，採用公對公杜邦線導向TFT，即可擁有與直接插上Pi相同的功能。接著找出TFT上NC的腳位來當作按鈕或是LED的訊號腳。</td>
	</tr>
	<tr>
		<td></td>
		<td>上傳至Facebook</td>
		<td>上網找了許多資料，我們也有找到網友分享的步驟，但因Facebook不斷的更新，以至於和分享的資料有落差。</td>
	</tr>
	<tr>
		<td>  ✔  </td>
		<td>觸控面板安裝、觸控</td>
		<td>在網路上找到一家網站的實作可以成功顯示樹莓的桌面，但卻一直無法觸控，經過不斷的重灌、除錯後，觸控功能總算是完成了。</td>
	</tr>
</table>
#### 二、 寫了什麼軟體或修改哪些設定
<table>
  <tr>
		<td>作用</td>
		<td>動作</td>
	</tr>
	<tr>
		<td>開機時將IP寄到信箱</td>
		<td>1. 撰寫寄IP到信箱程式。<br/>
		2. 修改該檔案的權限。<br/> 
		sudo chmod 755 sendip.sh<br/> 
		3. 設定該shell檔可以一開機就執行。<br/>
		sudo update-rc.d sendip.sh defaults。<br/> </td>
	</tr>
	<tr>
		<td>3</td>
		<td>4</td>
	</tr>
	<tr>
		<td>3</td>
		<td>4</td>
	</tr>
</table>

# 柒、 組裝過程及製作教學






# 捌、 操作教學




# 玖、 工作分配表
<table>
  <tr>
		<td>   </td>
		<td>吳宗翰</td>
		<td>高玟瑜</td>
	</tr>
	<tr>
		<td>電路銲接</td>
		<td>✔</td>
		<td></td>
	</tr>
	<tr>
		<td>麵包板電路設計</td>
		<td>✔</td>
		<td></td>
	</tr>
	<tr>
		<td>相關資料搜尋、彙整</td>
		<td></td>
		<td>✔</td>
	</tr>
	<tr>
		<td>程式撰寫</td>
		<td>✔</td>
		<td>✔</td>
	</tr>
	<tr>
		<td>外觀製作</td>
		<td></td>
		<td>✔</td>
	</tr>
	<tr>
		<td>文件處理</td>
		<td></td>
		<td>✔</td>
	</tr>
</table>





# 拾、 參考來源
1. 封面照片：
http://iguang.tw/gohappy/product/24955.html
2. Raspberry Pi最佳入門與實戰應用，碁峰資訊股份有限公司，2015年02月
3. 電路參考：
https://sites.google.com/site/raspberrypidiy/home
4. TFT畫面顯示：
http://mcuapps.com/blog/build-lcd-touchscreen-drivers-for-raspberry-pi
5. TFT面板觸控功能： <br/>
(1) http://mcuapps.com/blog/build-lcd-touchscreen-drivers-for-raspberry-pi <br/>
(2) http://www.geekfan.net/5618/
6. TFT面板與相機同步顯示：
https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam/pi-setup

<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.11.0" name="terrain" tilewidth="16" tileheight="16" tilecount="384" columns="24">
 <image source="../terrain.png" width="384" height="256"/>
 <tile id="1">
  <objectgroup draworder="index" id="2">
   <object id="1" x="5" y="9" width="11" height="7"/>
  </objectgroup>
 </tile>
 <tile id="2">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="8" width="16" height="8"/>
   <object id="2" x="0" y="8" width="16" height="8"/>
  </objectgroup>
 </tile>
 <tile id="3">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="9" width="11" height="7"/>
  </objectgroup>
 </tile>
 <tile id="25">
  <objectgroup draworder="index" id="2">
   <object id="1" x="3" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <tile id="27">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <tile id="28">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="5.09091" width="10.9091" height="10.9091"/>
  </objectgroup>
 </tile>
 <tile id="30">
  <objectgroup draworder="index" id="2">
   <object id="1" x="4.54545" y="4.90909" width="11.4545" height="11.0909"/>
  </objectgroup>
 </tile>
 <tile id="49">
  <objectgroup draworder="index" id="2">
   <object id="1" x="3" y="0" width="13" height="15"/>
  </objectgroup>
 </tile>
 <tile id="50">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0" width="16" height="16"/>
   <object id="2" x="0" y="0" width="16" height="16"/>
  </objectgroup>
 </tile>
 <tile id="51">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0" width="16.0909" height="15.9091"/>
   <object id="2" x="0" y="0" width="13" height="15"/>
  </objectgroup>
 </tile>
 <tile id="52">
  <objectgroup draworder="index" id="2">
   <object id="1" x="5.36364" y="0" width="10.8182" height="16"/>
   <object id="2" x="3" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <tile id="53">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <tile id="100">
  <objectgroup draworder="index" id="2">
   <object id="1" x="3" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <tile id="101">
  <objectgroup draworder="index" id="2">
   <object id="1" x="0" y="0" width="13" height="16"/>
  </objectgroup>
 </tile>
 <wangsets>
  <wangset name="dirt_terrain" type="corner" tile="-1">
   <wangcolor name="dirt_wall" color="#d19944" tile="-1" probability="1"/>
   <wangtile tileid="34" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="35" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="36" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="37" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="38" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="58" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="59" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="60" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="61" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="62" wangid="0,1,0,1,0,1,0,0"/>
   <wangtile tileid="82" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="83" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="84" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
  <wangset name="grass_mountain" type="corner" tile="-1">
   <wangcolor name="grass mountain" color="#396f3a" tile="-1" probability="1"/>
   <wangtile tileid="1" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="2" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="3" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="25" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="26" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="27" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="29" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="49" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="50" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="51" wangid="0,0,0,0,0,0,0,1"/>
   <wangtile tileid="74" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="75" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="98" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="99" wangid="0,1,0,1,0,1,0,0"/>
  </wangset>
 </wangsets>
</tileset>

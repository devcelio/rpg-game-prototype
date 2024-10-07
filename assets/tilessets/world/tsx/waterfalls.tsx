<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.11.0" name="waterfalls" tilewidth="16" tileheight="16" tilecount="336" columns="24">
 <image source="../waterfalls.png" width="384" height="224"/>
 <tile id="50">
  <animation>
   <frame tileid="50" duration="180"/>
   <frame tileid="98" duration="180"/>
   <frame tileid="146" duration="180"/>
  </animation>
 </tile>
 <tile id="51">
  <animation>
   <frame tileid="51" duration="180"/>
   <frame tileid="99" duration="180"/>
   <frame tileid="147" duration="180"/>
  </animation>
 </tile>
 <tile id="52">
  <animation>
   <frame tileid="52" duration="180"/>
   <frame tileid="100" duration="180"/>
   <frame tileid="148" duration="180"/>
  </animation>
 </tile>
 <tile id="74">
  <animation>
   <frame tileid="74" duration="180"/>
   <frame tileid="122" duration="180"/>
   <frame tileid="170" duration="180"/>
  </animation>
 </tile>
 <tile id="75">
  <animation>
   <frame tileid="75" duration="180"/>
   <frame tileid="123" duration="180"/>
   <frame tileid="171" duration="180"/>
  </animation>
 </tile>
 <tile id="76">
  <animation>
   <frame tileid="76" duration="180"/>
   <frame tileid="124" duration="180"/>
   <frame tileid="172" duration="180"/>
  </animation>
 </tile>
 <wangsets>
  <wangset name="water" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="54" wangid="0,0,0,1,0,0,0,0"/>
   <wangtile tileid="55" wangid="0,0,0,1,0,1,0,0"/>
   <wangtile tileid="56" wangid="0,0,0,0,0,1,0,0"/>
   <wangtile tileid="78" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="79" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="80" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="81" wangid="0,1,0,0,0,1,0,1"/>
   <wangtile tileid="82" wangid="0,1,0,1,0,0,0,1"/>
   <wangtile tileid="102" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="103" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="104" wangid="0,0,0,0,0,0,0,1"/>
   <wangtile tileid="105" wangid="0,0,0,1,0,1,0,1"/>
   <wangtile tileid="106" wangid="0,1,0,1,0,1,0,0"/>
  </wangset>
  <wangset name="waterfall" type="corner" tile="-1">
   <wangcolor name="" color="#ff0000" tile="-1" probability="1"/>
   <wangtile tileid="50" wangid="0,1,0,1,0,0,0,0"/>
   <wangtile tileid="51" wangid="0,1,0,1,0,1,0,1"/>
   <wangtile tileid="52" wangid="0,0,0,0,0,1,0,1"/>
   <wangtile tileid="74" wangid="0,1,0,0,0,0,0,0"/>
   <wangtile tileid="75" wangid="0,1,0,0,0,0,0,1"/>
   <wangtile tileid="76" wangid="0,0,0,0,0,0,0,1"/>
  </wangset>
 </wangsets>
</tileset>

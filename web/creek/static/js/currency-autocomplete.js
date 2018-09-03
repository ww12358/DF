$(function(){
  var symbols = [
    { value: 'A', data: 'Soybean 豆一' },
    { value: 'C', data: 'Corn 玉米' },
	{ value: 'M', data: 'Soybean Meal 豆粕' },
    { value: 'Y', data: 'Soybean Oil 豆油' },
    { value: 'P', data: 'Palm Oil 棕榈油' },
    { value: 'SR', data: 'Sugar 白糖' },
    { value: 'CF', data: 'Cotton 棉花' },
    { value: 'WH', data: 'Wheat 强麦' },
    { value: 'OI', data: 'Rap Oil 菜籽油' },
    { value: 'RM', data: 'Rapseed Meal 菜籽粕' },
    { value: 'RI', data: 'Early Indica Rice 早籼稻' },
    { value: 'CU', data: 'Copper 铜' },
    { value: 'AL', data: 'Aluminium  铝' },
    { value: 'ZN', data: 'Zinc 锌' },
    { value: 'FG', data: 'Glass 玻璃' },
    { value: 'PP', data: 'Polypropylene 聚丙烯' },
    { value: 'L', data: 'Polyethylene 聚乙烯' },
    { value: 'V', data: 'PVC 聚氯乙烯' },
    { value: 'I', data: 'Steel Stone 铁矿' },
    { value: 'J', data: 'Coke 焦炭' },
    { value: 'JM', data: 'Coking Coal 焦煤' },
    { value: 'IF', data: 'HuShen 300 Index 沪深300指数' },
    { value: 'IH', data: 'SSE 50 Index 上证50指数' },
    { value: 'IC', data: 'CSI 500 Indexhu' },
    { value: 'FER', data: 'Ferrous Idx 黑色金属' },
    { value: 'NON', data: 'Nonferrous Idx 有色金属' },
    { value: 'CON', data: 'Construction Idx' },
    { value: 'COA', data: 'Coal Idx 煤炭指数' },
    { value: 'GRA', data: 'Grain Idx 谷物' },
    { value: 'FEE', data: 'Feed Crop Idx 饲料指数' },
    { value: 'SOY', data: 'Soybean Idx 大豆指数' },
    { value: 'OIL', data: 'Oil Idx 油脂指数' },
    { value: 'SOF', data: 'Soft Idx 软商品' },
    { value: 'CHE', data: 'Energy Chemical Idx 能源化工' },
    { value: 'IND', data: 'Industry Idx 工业' },
    { value: 'ALG', data: 'Algriculture Idx 农业' },
    { value: 'EQU', data: 'Equity Idx 证券资产' },
    { value: 'DCE', data: 'DCE Idx 大连' },
    { value: 'CZE', data: 'CZE Idx 郑州' },
    { value: 'SHF', data: 'SHF Idx 上海' },
    { value: 'CHN', data: 'China Comm. Index 中国' }
  ];

  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: symbols,
    onSelect: function (suggestion) {
      var thehtml = '<strong>Symbol:</strong>' + suggestion.value + '<br><strong>Description:</strong> ' + suggestion.data;
      $('#outputcontent').html(thehtml);
    }
  });
  

});
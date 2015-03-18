$(function(){
	var stat = [];
	var a = $('.move_box a');
	var opacity = [0.2,0,0.2];
	var timer = null;

	a.each(function(i){
		stat[i] = {
			'w' : $(this).width(),
			'h' : $(this).height(),
			'l' : $(this).position().left,
			't' : $(this).position().top,
			'z' : $(this).css('z-index'),
			'op' : opacity[i],
			'index' : $(this).index()
		}
	})

	var timer = setInterval(function(){
		move();
	},2000)

	function move(){
		a.each(function(i){
			stat[i].index++;
			if(stat[i].index > 2){
				stat[i].index = 0;
			}
			var next = stat[i].index;
			$(this).css('z-index', stat[next].z).animate({
				'width' : stat[next].w,
				'height': stat[next].h,
				'left': stat[next].l,
				'top': stat[next].t
			}).find('b').css('opacity', stat[next].op);
		})
	}

	$('.move_box').hover(function() {
		clearInterval(timer);
	}, function() {
		timer = setInterval(function(){
			move();
		},2000)
	});



})
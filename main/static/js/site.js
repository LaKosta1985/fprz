 var rect = document.querySelectorAll(".randomImg");
 
rect.forEach(item=>item.addEventListener("click", function () { 
	 var SrcItem =event.target.getAttribute('src');
  

}));


 (function ($) {

        $('.swipebox').swipebox();

    })(jQuery);


$(document).ready(function () {
	

		$('.content_toggle').click(function (event) {
			event.preventDefault();   // блокировать переход по ссылке

			const $link = $(event.target); // a - конкретная ссылка которая была нажата
			const $content = $link.prev('div.content_block');  // div -контент блок перед ссылкой

			$content.toggleClass('hide'); // показать или скрыть контент блок

			const htmlLink = $content.hasClass('hide') ? 'Подробнее' : 'Скрыть';
			$link.html(htmlLink);
		});
	});

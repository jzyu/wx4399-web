/**
 * Created by hp on 2015/5/8.
 */

// -- 设定按钮组：打勾、添加active class，并设置click回调函数 --
//group: 按钮组元素选择器
//buttonClick: 点击处理回调函数
function initButtonGroup(group, actived_index, buttonClick) {
    console.log('initButtonGroup: size = ' + group.size());
    group.eq(actived_index).addClass("active").append('<span>&#10004</span>'); //actived项打勾

    group.click(function () {
        console.log('click element = ' + $(this).html());
        //清除原来的active，设置新的
        group.filter('.active').removeClass('active');
        $(this).addClass('active');

        //清除原来的打勾，设置新的
        group.children('span').remove();
        $(this).append('<span>&#10004</span>');

        buttonClick(group.index($(this)));
    });
}
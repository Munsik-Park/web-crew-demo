// script.js

document.addEventListener('DOMContentLoaded', function() {
    // 모든 링크에 대한 클릭 이벤트 리스너를 추가합니다.
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                // 부드러운 스크롤 효과를 구현합니다.
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});
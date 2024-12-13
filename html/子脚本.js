
(async function () {
    'use strict';

    // 页面刷新函数
    function refreshPage() {
        window.location.reload();
    }

    // 主页面逻辑
    function handleMainPage() {
        const unfinishedItems = document.querySelectorAll('.item-infos.default');
        if (unfinishedItems.length > 0) {
            unfinishedItems[0].previousElementSibling.click();
            setTimeout(refreshPage, 300000);
            clearInterval(intervalId);
        } else {
            const nextPageBtn = document.querySelector('.ivu-page-next');
            if (nextPageBtn) nextPageBtn.click();
        }
    }

    // 等待函数
    function waitTimeout(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // 次页面逻辑
    async function handleSubPage() {
        const infoRate = document.querySelector('.scoring-wrapper .info-rate:not([style*="display: none"])');
        const submitButton = Array.from(document.querySelectorAll('button')).find(el => el.textContent.trim() === "提交");

        if (infoRate && submitButton) {
            const rateItem = infoRate.querySelector('.rate-item:last-child');
            if (rateItem) {
                rateItem.dispatchEvent(new MouseEvent("mouseleave", { bubbles: true }));
                await waitTimeout(500);
                rateItem.click();
                await waitTimeout(500);
                submitButton.click();
            } else {
                console.error("评分星星未找到！");
            }
        } else {
            console.error("评分区域或提交按钮未找到！");
        }

        const continueBtn = document.querySelector('.text');
        if (continueBtn) continueBtn.click();

        const video = document.querySelector('video');
        if (video) {
            video.volume = 0;
            if (video.ended) {
                const replayBtn = document.querySelector('.replay');
                if (replayBtn) replayBtn.click();
            }
        } else {
            const nextBtn = document.querySelector('.next');
            if (nextBtn) nextBtn.click();
        }
    }

    // 自动化任务
    async function automationTask() {
        if (document.URL.includes('train2')) {
            handleMainPage();
        } else if (document.URL.includes('grain')) {
            await handleSubPage();
        }
    }

    const intervalId = setInterval(automationTask, 3000);
})();
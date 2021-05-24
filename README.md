# advCAPTCHA

## audio captcha tasks
### Example Audio
- `static/prototpypes/example/example.wav`
### Audio CAPTCHA Tasks
- 在 `static/prototpypes`中，所有的題目會以壓縮檔 `[timestamp].tar` 的形式傳入 testbed server
- 解壓縮：`tar -xvf [timestamp].tar`
- 壓縮黨中包含：
    - 以 pid 做為區隔之個別 audio tasks，其中包含所有 audio tasks 音檔 (e.g. task1_1.wav) 以及 `task_info.tsv` 紀錄所有 task 的資訊
    - `participants_task_ordering_[timestamp].tsv` 中包含所有 pid 的 task order 資訊
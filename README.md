# tigermm-skills

MARY III 的技能市场（Skill Market）—— 一小组可直接安装的 Python 技能。

每个技能就是一个独立的 `.py` 文件，暴露两个函数。装进 Agent 之后，它就能被自然语言触发。

## 技能格式

```python
def skill_info():
    return {"name": "...", "desc": "...", "tags": [...], "triggers": [...]}

def execute(args):
    # args 是一个 dict，返回字符串
    return "结果"
```

- `skill_info()` 告诉 Agent 这个技能叫什么、什么时候该用它（`triggers` 是触发词）
- `execute(args)` 是干活的地方

## 安装

在 MARY III 里直接拉：

```
/market install https://raw.githubusercontent.com/yunqingtao/tigermm-skills/main/weather.py
```

`catalog.json` 里有全部 10 个技能的名称、说明和安装地址，按它遍历即可。

## 技能一览

| 技能 | 文件 | 说明 |
|---|---|---|
| weather | `weather.py` | 查天气，走 wttr.in（默认城市 Jinan） |
| calculator | `calculator.py` | 算数学表达式 |
| translator | `translator.py` | ⚠️ **占位，尚未实现**（见下） |
| password_gen | `password_gen.py` | 生成随机密码，用 `secrets` 而非 `random` |
| json_formatter | `json_formatter.py` | JSON 格式化与校验 |
| timer | `timer.py` | 倒计时 |
| clipboard | `clipboard.py` | 读写系统剪贴板（仅 Windows） |
| qr_code | `qr_code.py` | 生成二维码链接 |
| markdown_preview | `markdown_preview.py` | Markdown 转 HTML |
| http_tester | `http_tester.py` | 测 HTTP 接口并格式化返回 |

## 先把话说清楚（免得你装完发现不对）

这些是很小的工具脚本，不是生产级组件。几个已知的坑：

- **calculator** 用 `eval()` 在受限命名空间里求值。玩具级实现，**不要**拿它跑不受信任的输入。
- **clipboard** 只支持 Windows（依赖 `clip` 和 PowerShell 的 `Get-Clipboard`）；其他系统会返回一句失败提示。
- **qr_code** 不在本地生成图片 —— 它只是拼一个 `api.qrserver.com` 的 URL。**你传进去的文字会发给那个第三方服务。**
- **timer** 会真的 `time.sleep()` 阻塞到倒计时结束。在 Agent 里调用它，会卡住那么久。
- **weather** 需要联网，且没做错误处理（断网会直接抛异常）。
- **markdown_preview** 依赖 `markdown` 这个第三方库；没装的话会退化成「去掉 # 再包个 `<h1>`」。
- **http_tester** 会对传入的任意 URL 发请求。

## translator 是占位

`translator.py` 目前**不会翻译**。它只返回一句：

```
Translation service ready. Use: execute({'text':'hello','from':'en','to':'zh'})
```

也就是说 `catalog.json` 里原来那句说明（"Simple translator using free API"）与代码不符，已改掉。要真做翻译，需要在 `execute()` 里接一个翻译服务；欢迎 PR。

## 许可

MIT，见 [LICENSE](LICENSE)。

这些脚本按原样提供、不作任何担保。用之前自己扫一眼代码 —— 总共也就十几行一个。

import execjs
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'LOGIN_STATUS=1; pwa2=%220%7C0%7C3%7C1%22; my_rd=2; passport_assist_user=CkHELg7w1OVu6PiFy178XEtkBZl5X7sYQEs9sV1tmTSi6Sn0OFEml8HmmQSN3wbGWPmPblcJC5io7-8kAYTKyEnilRpKCjzkH7TwnQE-UIA7KmP9skw234jVA0QMBFW3BQz7QBlGEi94WxxV4W25zYzMhD5zfXCclZyfVBm5fVArLo4Q9ZvKDRiJr9ZUIAEiAQNrMmyD; n_mh=X7K6S_xLnxsPog9H3rAAdgcS97nYnVWkjXOwnnBUJ24; sid_guard=93b1357b4e2a270f714811e616f31d0d%7C1708738110%7C5183997%7CWed%2C+24-Apr-2024+01%3A28%3A27+GMT; odin_tt=cb639a78a5ee3a4fba15d89ade6fef40865a5ee9ce3087fd7014b2503de996f83a879ed2f6c6f75202cf2de2ff606cc5; ttwid=1%7COGij4KwNAkGXwuxz5TfMUAA2frV9GQbUafQNetvDT_s%7C1716902206%7C9162a097f63ab9feae327e1e184ad305cf6aa876d7522d4a7414f79d81caa8d9; s_v_web_id=verify_lwqf8x28_iUnPUhtP_ZBp4_4M1d_BYQ2_ubqYNhKq91xx; passport_csrf_token=1d615ce78429995b75f5e7ee9b738b66; passport_csrf_token_default=1d615ce78429995b75f5e7ee9b738b66; bd_ticket_guard_client_web_domain=2; __ac_nonce=06672c3d400a18ef5b637; __ac_signature=_02B4Z6wo00f01GR5L4AAAIDAU13r3m..mtRkWSsAAH9094; UIFID_TEMP=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e3852806c0afa6f5cd03e709b1c623106bcfc56f8fc143149fcde1c19ccb10ac9fd34156b2be6755c441c885af8d01b703855cedf240894d2161a66db30b5b22ba64bbbac1d55401620b67f247aeb3e6e5a9de3; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1920; dy_sheight=1080; csrf_session_id=07d240eee1bf08507cde83432713b5b0; fpk1=U2FsdGVkX1+yuJGgOiisuCp0Om3MIPf7keZqcbnQJT9fH8ROFKHiIn0UDXJUJrXqaXkMqZwtpGbL4vTKG4RrlA==; fpk2=5f4591689f71924dbd1e95e47aec4ed7; strategyABtestKey=%221718797270.369%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A1%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; UIFID=c4683e1a43ffa6bc6852097c712d14b81f04bc9b5ca6d30214b0e66b4e3852806c0afa6f5cd03e709b1c623106bcfc56f8fc143149fcde1c19ccb10ac9fd341576d5b9202b45338f8715a87c1cea95bfa55ccd70b680824609419fae8e86c8b8fc1503dfb0c92991e54e86c092e269924a7de8351d3e53a155fefc7b450b9f0ce7c63ba1bb8b3f59ccef6c02ef7a163dc598cb1b6f29dee39882f89c302702570663cc976a5d23c708324559b4c57b4b58ea27103559c7b6de7854f05e2fc1fb; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; download_guide=%222%2F20240619%2F0%22; WallpaperGuide=%7B%22showTime%22%3A1718797470997%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A7%2C%22cursor2%22%3A0%7D; IsDouyinActive=true; msToken=Pq-nrh-UlXBKSJD_UPDdeQE7YRj2SX0xwOlLJetWtS-gX3AcTBXkvldhl9VPX-KROfgZQ0tb5dRxsmi6HL1yZbIN7dlmaGeHVM69T0uW3tmzvebkJeMZUaDQIo0biQ==; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRkFxNXNOMGs4eUg4TEgrWnFoeENEcXhmSS9qUDZ6aVZLZGN2Unh1Mk1SemFsaDdCd3daRlJTSTAweGZRUWZPTFY0c3kyZ3hLU1lNT2ZNb09aVnlQdkE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; home_can_add_dy_2_desktop=%221%22',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/user/MS4wLjABAAAACvcqXxRuFEOG23oFraXLb4WBMiZrYL5Yx27aKuQvVxrmAYOrrFOdfKLp_kESkGE7?vid=7379524239407205684',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}

params = {
    'device_platform': 'webapp',
    'aid': '6383',
    'channel': 'channel_pc_web',
    'sec_user_id': 'MS4wLjABAAAAqrhPpbcXVe6oLwmgdv-RYq-YkzEXynLeypM9GAoG04bJgK09Qu5Iy-KkPciAEXQR',
    'max_cursor': '1718017810000',
    'locate_item_id': '7353313373536128292',
    'locate_query': 'false',
    'show_live_replay_strategy': '1',
    'need_time_list': '0',
    'time_list_query': '0',
    'whale_cut_token': '',
    'cut_version': '1',
    'count': '18',
    'publish_video_strategy_type': '2',
    'update_version_code': '170400',
    'pc_client_type': '1',
    'version_code': '290100',
    'version_name': '29.1.0',
    'cookie_enabled': 'true',
    'screen_width': '1920',
    'screen_height': '1080',
    'browser_language': 'zh-CN',
    'browser_platform': 'Win32',
    'browser_name': 'Edge',
    'browser_version': '126.0.0.0',
    'browser_online': 'true',
    'engine_name': 'Blink',
    'engine_version': '126.0.0.0',
    'os_name': 'Windows',
    'os_version': '10',
    'cpu_core_num': '16',
    'device_memory': '8',
    'platform': 'PC',
    'downlink': '10',
    'effective_type': '4g',
    'round_trip_time': '50',
    # 'webid': '7374038737356113442',
    'verifyFp': 'verify_lwqf8x28_iUnPUhtP_ZBp4_4M1d_BYQ2_ubqYNhKq91xx',
    'fp': 'verify_lwqf8x28_iUnPUhtP_ZBp4_4M1d_BYQ2_ubqYNhKq91xx',
    'msToken': 'NjEMDSI35ye3TJPjJpnWf3-exbXnfHn-A5ZxcMO_XSNxQrG7zpTCgg7-NQFPQ5QYzKOzan1d8ZSAQV56UHZdg4_ryxc2D8dx8URJiPy3EgzsAUb8D3JQWLbhz9Hhcg==',
    'a_bogus': 'Y780/m0DDE6TvfWX5-VLfY3q6Ur3Y8uN0trEMD2fZVVTPy39HMOf9exETjzv4jjjNs/DIe8jy4hjT3PMx5InA3vRHuDKUIcpmDSkKl5Q-oW75NiHCybBE0hO-ib3SFa/5XNAxc40y75azYT0AoKJ5kI6PjCja3Lk96EtrNqL2oMA',

}

baseurl='https://www.douyin.com/aweme/v1/web/aweme/post?'
params_url="device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAACvcqXxRuFEOG23oFraXLb4WBMiZrYL5Yx27aKuQvVxrmAYOrrFOdfKLp_kESkGE7&max_cursor=1700210098000&locate_item_id=7379524239407205684&locate_query=false&show_live_replay_strategy=1&need_time_list=0&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&update_version_code=170400&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=126.0.0.0&browser_online=true&engine_name=Blink&engine_version=126.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7374038737356113442&verifyFp=verify_lwqf8x28_iUnPUhtP_ZBp4_4M1d_BYQ2_ubqYNhKq91xx&fp=verify_lwqf8x28_iUnPUhtP_ZBp4_4M1d_BYQ2_ubqYNhKq91xx&msToken=qYC28UmfMBi6y_LLQuOnMPB5gApKZ8bb40P0GqNf1PTkLjGL6a6TqTCLo4f8DeKo_yEFlpllMukarBqNEdsRZ7viQN1cnIhNt-tmJfCIvxupO5QaNspqT-9ZMWTcbQ%3D%3D"
url=baseurl+params_url
print(url)
print(params_url)
js_code=execjs.compile(open("抖音.js",encoding='utf-8').read())
a_bogus=js_code.call("aa",params_url)
print(a_bogus)
whole_url=url+"&a_bogus="+str(a_bogus)
print(whole_url)
response = requests.get(whole_url, headers=headers)
print(response.text)
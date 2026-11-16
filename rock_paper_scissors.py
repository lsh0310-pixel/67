import random

# 使用最外層迴圈實現「再玩一次」功能
while True:
    print("\n=== ✊✋✌️ 剪刀石頭布 終極大對決 (五勝挑戰) ===")

    # 1. 冒險者登入
    name = input("請輸入你的冒險者名字：")

    # 2. 裝備選擇 (新增 3 項裝備選擇功能)
    print("\n⚔️ 請選擇你的裝備（輸入數字 1~3）：")
    print("1. 🍀 幸運護符（平手時，直接判定你獲勝得分！）")
    print("2. 🗡️ 雙倍聖劍（獲勝時，有 50% 機率直接獲得 2 勝！）")
    print("3. 🛡️ 防禦盾牌（獲得 1 次抵擋電腦得分的護盾！）")

    eq_choice = input("請選擇裝備編號 (1-3)：")

    if eq_choice == "1":
        equipment = "幸運護符"
    elif eq_choice == "2":
        equipment = "雙倍聖劍"
    elif eq_choice == "3":
        equipment = "防禦盾牌"
    else:
        equipment = "新手木棒"
        print("⚠️ 輸入無效，預設裝備為：新手木棒（無特殊效果）")

    # 盾牌狀態初始化
    has_shield = True if equipment == "防禦盾牌" else False

    # 印出前置劇情
    print("\n=== 系統廣播 ===")
    print(f"歡迎勇敢的冒險者【{name}】！")
    print(f"你已經裝備了【{equipment}】，準備好迎接第一關的 【猜拳】 挑戰！")
    print("規則：先獲得 5 勝的一方就是最終贏家！\n")

    # 戰鬥前置作業
    player_wins = 0
    computer_wins = 0
    round_num = 1
    options = ["剪刀", "石頭", "布"]

    # 3. 迴圈條件設定：改為 < 5 勝
    while player_wins < 5 and computer_wins < 5:
        print(f"--- 第 {round_num} 回合 ---")
        print(f"🏆 目前戰況 - 你：{player_wins} 勝 | 電腦：{computer_wins} 勝")

        player_choice = input("請出拳 (輸入 剪刀、石頭 或 布)：")

        # 檢查玩家是否輸入錯誤
        if player_choice not in options:
            print("⚠️ 哎呀！指令錯誤，請輸入 剪刀、石頭 或 布。\n")
            continue

        computer_choice = random.choice(options)
        print(f"🤖 電腦出了：{computer_choice}")

        # 4. 勝負判斷與裝備能力觸發
        if player_choice == computer_choice:
            if equipment == "幸運護符":
                print("✨【幸運護符】發動效果！平手強制判定為你獲勝！\n")
                player_wins += 1
            else:
                print("平手！沒有人得分。\n")

        elif (player_choice == "剪刀" and computer_choice == "布") or \
             (player_choice == "石頭" and computer_choice == "剪刀") or \
             (player_choice == "布" and computer_choice == "石頭"):

            if equipment == "雙倍聖劍" and random.random() < 0.5:
                print("🗡️【雙倍聖劍】觸發暴擊！本回合直接獲得 2 分！\n")
                player_wins += 2
            else:
                print("🎉 這回合你贏了！\n")
                player_wins += 1

        else:
            if equipment == "防禦盾牌" and has_shield:
                print("🛡️【防禦盾牌】發動效果！成功抵擋了電腦本次得分！\n")
                has_shield = False  # 護盾使用後失效
            else:
                print("💥 這回合電腦贏了！\n")
                computer_wins += 1

        round_num += 1

    # 5. 最終結算
    print("=== 🌟 最終結果 🌟 ===")
    if player_wins >= 5:
        print(f"🏆 恭喜你以 {player_wins} : {computer_wins} 擊敗了電腦，成為剪刀石頭布大師！")
    else:
        print(f"💻 很可惜，電腦以 {computer_wins} : {player_wins} 獲得了最終勝利，下次再來挑戰吧！")

    # 6. 再玩一次功能
    play_again = input("\n🎮 是否要再玩一次？(輸入 y 重新開始，輸入其他任意鍵離開)：").lower()
    if play_again != 'y':
        print("\n感謝遊玩，冒險者下次見！👋")
        break  # 結束最外層迴圈，離開遊戲

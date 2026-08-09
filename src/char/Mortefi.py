
import time

from src.char.BaseChar import BaseChar


class Mortefi(BaseChar):
    """莫特斐(副C辅助): 快速攒协奏 -> 满协奏切人, 把延奏(重击伤害加深38%)
    传给主C(嘉贝莉娜)。

    依据库街区官方轮椅轴:
      【莫特斐】: A-E-R-AAAA-E-Q (满协奏切人)
    要点:
      1. 进场 A 起手, E(龙息回旋) -> R(解放) -> AAAA -> E -> Q;
      2. 必须满协奏才切人(原版放完技能直接切, 协奏不满时延奏
         根本给不出去, 重击+38% 等于浪费);
      3. 满回路可用时强化技能优先(快速协奏定位)。
    """

    def do_perform(self):
        self.wait_down()
        # 官方轮椅轴: A-E-R-AAAA-E-Q (满协奏切人)
        self.continues_normal_attack(0.3)
        self.click_resonance()
        if not self.click_liberation():
            self.click_liberation(wait_if_cd_ready=1)
        self.continues_normal_attack(0.8)
        self.click_resonance()
        self.click_echo()
        # 协奏未满则继续普攻攒, 满协奏或超时才切人(保证延奏给主C)
        start = time.time()
        while not self.is_con_full() and time.time() - start < 5:
            if self.need_fast_perform():
                break
            self.continues_normal_attack(0.5)
            self.check_combat()
        self.switch_next_char()

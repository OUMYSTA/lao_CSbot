<script setup lang="ts">
import { ref } from 'vue'

interface ExampleList {
  header: string
  question1: string
  question2: string
}

const examples = ref<ExampleList[]>([
  {
    header: '1. ຊື່ຫຼັກສູດ',
    question1: '- ຊື່ຫຼັກສູດພາສາລາວຂອງຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີແມ່ນຫຍັງ',
    question2: '- ຊື່ຫຼັກສູດພາສາອັງກິດຂອງຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີແມ່ນຫຍັງ'
  },
  {
    header: '2. ການເຂົ້າສຶກສາ',
    question1: '- ຖ້າຈະເຂົ້າຮຽນຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີຕ້ອງມີເງື່ອນໄຂໃດແດ',
    question2: '- ຖ້າຈະເຂົ້າຮຽນຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີຕ້ອງເຮັດແນວໃດ'
  },
  {
    header: '3. ເວລາຮຽນ',
    question1: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີຮຽນຈັກມື້',
    question2: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີຮຽນມື້ໃດແດ່'
  },
  {
    header: '4. ວິຊາຮຽນ',
    question1: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີປີ1 ພາກຮຽນ1 ຮຽນວິຊາຫຍັງແດ່',
    question2: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີປີ1 ພາກຮຽນ2 ຮຽນວິຊາຫຍັງແດ່'
  },
  {
    header: '5. ຈຳນວນໜ່ວຍກິດ',
    question1: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີມີຈັກໜ່ວຍກິດ',
    question2: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີປີ1ມີຈັກໜ່ວຍກິດ'
  },
  {
    header: '6. ຄ່າຮຽນ',
    question1: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີຄ່າຮຽນເທົ່າໃດ',
    question2: '- ຫຼັກສູດປະລິນຍາຕີສາຂາວິທະຍາສາດຄອມພິວເຕີປີ1 ຄ່າຮຽນເທົ່າໃດ'
  }
])

interface HowtoList {
  header: string
  image: string
}

const howto = ref<HowtoList[]>([
  {
    header: '1. ປ້ອນຄຳຖາມ',
    image: '../assets/input.png'
  },
  {
    header: '2. ເລືອກຄຳຖາມທີ່ແນະນຳຂຶ້ນມາ',
    image: '../assets/select.png'
  },
  {
    header: '3. ລໍຖ້າລະບົບປະມວນຜົນ',
    image: '../assets/process.png'
  },
  {
    header: '4. ຄຳຕອບທີ່ໄດ້ຈາກການປະມວນຜົນ',
    image: '../assets/output.jpeg'
  }
])
</script>

<template>
  <div class="px-10 carousel carousel-vertical h-[28rem] overflow-y-auto">
    <div class="carousel-item flex-col">
      <h1 class="text-2xl font-bold py-8">ຄູ່ມືແນະນຳການນຳໃຊ້ເວັບໄຊ</h1>
      <p>
        ເວັບໄຊແຊັດບອດໃຫ້ຂໍ້ມູນກ່ຽວກັບຫຼັກສູດພາກວິຊາວິທະຍາສາດຄອມພິວເຕີ
        ເປັນການໃຫ້ຂໍ້ມູນທົ່ວໄປຂອງແຕ່ລະຫຼັກສູດສາຂາຮຽນໃນພາກວິຊາວິທະຍາສາດຄອມພິວເຕີ,
        ຄະນະວິທະຍາສາດທຳມະຊາດ, ມະຫາວິທະຍາໄລແຫ່ງຊາດລາວ, ເຊິ່ງປະກອບມີຫຼັກສູດການສຶກສາດັ່ງນີ້:
      </p>
      <ul class="list-decimal pt-3 text-left px-48">
        <li>ຫຼັກສູດປະລິນຍາໂທ ສາຂາວິທະຍາສາດຄອມພິວເຕີ</li>
        <li>ຫຼັກສູດປະລິນຍາຕີ ສາຂາວິທະຍາສາດຄອມພິວເຕີ</li>
        <li>ຫຼັກສູດປະລິນຍາຕີ ສາຂາການພັດທະນາເວັບໄຊ</li>
        <li>ຫຼັກສູດປະລິນຍາຕີ ສາຂາການພັດທະນາໂປຣແກຣມຄອມພິວເຕີ</li>
        <li>ຫຼັກສູດຕໍ່ເນື່ອງປະລິນຍາຕີ ສາຂາວິທະຍາສາດຄອມພິວເຕີ</li>
      </ul>
      <h2 class="text-xl font-semibold pt-12 text-left">ຕົວຢ່າງການຕັ້ງຄຳຖາມ</h2>
      <ul class="text-left">
        <li v-for="(exam, idx) in examples" :key="idx">
          <h3 class="text-lg font-medium pb-1 pt-3">{{ exam.header }}</h3>
          <p>{{ exam.question1 }}</p>
          <p>{{ exam.question2 }}</p>
        </li>
      </ul>
      <h2 class="text-xl font-semibold pt-12 text-left">ການນຳໃຊ້ເວັບໄຊ</h2>
      <ul class="text-left">
        <li>
          <h3 class="text-lg font-medium pb-2 pt-5">1. ປ້ອນຄຳຖາມ</h3>
          <img src="../assets/input.png"/>
        </li>
        <li>
          <h3 class="text-lg font-medium pb-2 pt-5">2. ເລືອກຄຳຖາມທີ່ແນະນຳຂຶ້ນມາ</h3>
          <img src="../assets/select.png"/>
        </li>
        <li>
          <h3 class="text-lg font-medium pb-2 pt-5">3. ລໍຖ້າລະບົບປະມວນຜົນ</h3>
          <img src="../assets/process.png"/>
        </li>
        <li>
          <h3 class="text-lg font-medium pb-2 pt-5">4. ຄຳຕອບທີ່ໄດ້ຈາກການປະມວນຜົນ</h3>
          <img src="../assets/output.jpeg"/>
        </li>
        <!-- <li v-for="(how, idx) in howto" :key="idx">
          <h3 class="text-lg font-medium pb-1 pt-3">
            {{ how.header }}
          </h3>
          <img :src="how.image" alt="" class="w-32">
          <img src="../assets/1.png" alt="" class="w-[42rem]" />
        </li> -->
      </ul>
      <p class="text-gray-400 text-sm py-20">
        *ຂໍ້ມູນສຶກສາທີ່ນຳມາໃຊ້ໃນການພັດທະນາແຊັດບອດຄັ້ງນີ້ແມ່ນຂໍ້ມູນຫຼັກສູດປິ 2022 ແລະ ຂໍ້ມູນວິຊາຮຽນປີ
        2024
      </p>
    </div>
  </div>
</template>
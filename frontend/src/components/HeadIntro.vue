<script setup lang="ts">
import { ref, onMounted } from 'vue';
import HowTo from './HowTo.vue';

const hintText = ref('ຄຳແນະນຳສຳລັບການໃຊ້ງານ');

// Remove hint text after 3 seconds
onMounted(() => {
  setTimeout(() => {
    hintText.value = '';
  }, 3000);
});
</script>

<template>
  <div class="py-4 flex text-center md:flex justify-around bg-gray-600 shadow-md">
    <div class="w-32 h-32 m-4">
      <img
        src="https://th.bing.com/th/id/OIP.-ysyjL4c-hk3a1iXE9bpxwHaHa?rs=1&pid=ImgDetMain"
        alt="logo"
        class="rounded-full"
      />
    </div>
    <div class="pt-12 font-bold pr-14 text-xl flex flex-col gap-4 items-center text-white">
      <div>
        ການພັດທະນາແຊັດບັອດເຂົ້າໃນຂົງເຂດການສຶກສາໂດຍນຳໃຊ້ເຕັກນິກການປະມວນຜົນພາສາທຳມະຊາດ ກໍລະນີສຶກສາ:
        ພາກວິຊາວິທະຍາສາດຄອມພິວເຕີ
      </div>
      <div>
        Developing Chatbot for Education using Natural Language Processing Case Study: Department of
        Computer Science
      </div>
    </div>
    <button class="btn btn-circle btn-ghost mr-2" onclick="my_modal.showModal()">
      <img
        src="https://img.icons8.com/?size=100&id=98973&format=png&color=FFFFFF"
        alt="how to"
        width="22px"
        height="22px"
      />
      <span v-if="hintText" class="absolute mt-18 mr-24 w-32 bg-white text-xs px-2 py-1 rounded">
        {{ hintText }}
      </span>
    </button>
    <dialog id="my_modal" class="modal">
      <div class=" bg-white w-[52rem] h-[35rem] rounded-xl">
        <div class="modal_box pt-5">
          <HowTo />
        </div>
        <div class="modal-action flex justify-center">
          <form method="dialog">
            <button class="btn btn-warning">ປິດ</button>
          </form>
        </div>
      </div>
    </dialog>
  </div>
</template>
<script setup lang="ts">
import HowTo from './HowTo.vue'
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
    <button class="btn btn-circle bg-white mr-2" onclick="my_modal.showModal()">
      <img
        src="https://img.icons8.com/?size=100&id=7874&format=png&color=000000"
        alt="how to"
        width="22px"
        height="22px"
      />
    </button>
    <dialog id="my_modal" class="modal bg-white w-[52rem] h-[42rem] rounded-xl">
      <div class="modal_box">
        <HowTo />
      </div>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn btn-warning my-5">ປິດ</button>
        </form>
      </div>
    </dialog>
    <!-- <div class="dropdown dropdown-end">
      <div tabindex="0" role="button" class="btn btn-ghost btn-circle mr-2 bg-white">
        <div class="rounded-full">
          <img
            src="https://img.icons8.com/?size=100&id=7874&format=png&color=000000"
            alt="how to"
            width="22px"
            height="22px"
          />
        </div>
      </div>
      <ul tabindex="0" class="menu menu-sm dropdown-content rounded-md z-[1] bg-white mt-3 w-96 p-2 shadow">
        <HowTo/>
      </ul>
    </div> -->
  </div>
</template>

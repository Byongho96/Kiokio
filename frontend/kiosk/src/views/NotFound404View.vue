<template>
  <div class="w-100 h-100 bg-white">
    <div
      class="h-100 w-100 d-flex flex-column justify-content-center align-items-center"
    >
      <span style="font-size: 8vh"
        ><font-awesome-icon icon="fa-solid fa-circle-exclamation"
      /></span>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <p style="font-size: 2vh">
        <span>{{ address }}</span
        >에 오타가 있는지 확인하세요.
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFound404View',
  data() {
    return {
      address: window.location.href,
    }
  },
}
</script>

<style></style>

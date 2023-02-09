<template>
  <div>
    <v-parallax src="@/assets/background-home.png">
      <div class="center">
        <v-card
      class="d-flex flex-column justify-center mb-6 mt-16 pa-4"
      flat
      tile
    >
    <h2 class="text-center">🅀🅄🄸🅉🅉🄵🄸🄻🄼🄴</h2>
    <p class="text-center">Este quizz de personalidade foi desenvolvido para ajudá-lo a encontrar filmes 
      que correspondam ao seu estilo, gostos e interesses.</p>
    <v-btn
            color="primary"
            :to="{ name: 'quizz' }"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4">
            <v-icon icon="mdi-speedometer" size="large" start />
            Get Started
          </v-btn>
    </v-card>
      </div>
    </v-parallax>
  </div>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>
<style scoped>
.center{
  margin: 400px;
  background: rgba(0, 0, 0, 0.33);
  border-radius: 29px;
}
</style>

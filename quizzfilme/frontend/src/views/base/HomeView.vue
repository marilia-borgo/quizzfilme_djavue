<template>
  <div>
    <v-parallax src="@/assets/background-home.png">
      <div class="center">
        <v-card
      class="d-flex flex-column justify-center mb-6 mt-16 pa-4"
      flat
      tile
      style=" background: rgba(0, 0, 0, 0.33);"
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
          <v-btn
            v-if="!loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4 ml-3">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
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
  border-radius: 29px;
}
</style>

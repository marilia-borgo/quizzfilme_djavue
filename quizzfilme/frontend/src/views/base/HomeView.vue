<template>
  <v-container class="fill-height">
    <div
    class="d-flex justify-center mb-10 mt-10"
    >
      <h1>🅀🅄🄸🅉🅉🄵🄸🄻🄼🄴</h1>
   </div>
    <div>
      <h2 class="mb-5"> Este quizz de personalidade foi 
        desenvolvido para ajudá-lo a encontrar filmes qu
        e correspondam ao seu estilo, gostos e interesses. </h2>

      <h3 class="mb-5">Basta responder a algumas perguntas simples sobre suas preferências e valores, 
        e em poucos minutos você terá uma lista de sugestões de filmes para assistir. </h3>

       <h1>Então, vamos começar e descobrir quais filmes são perfeitos para você!</h1>
    </div>
      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
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
          <v-btn
            v-else
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
          <v-btn
            v-if="loggedUser"
            color="primary"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'quizz' }"
            class="my-4">
            <v-icon icon="mdi-folder-star-multiple" size="large" start />
            tarefas
          </v-btn>
        </v-col>
      </v-row>
  </v-container>
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

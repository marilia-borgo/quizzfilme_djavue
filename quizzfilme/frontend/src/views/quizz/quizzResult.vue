<template>
  <v-card
    class="mx-auto"
    max-width="900"
  >
    <v-img
      class="align-end text-white"
      height="200"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
      cover
    >
      <v-card-title>{{resultado.resultado}}</v-card-title>
    </v-img>

    <v-card-subtitle class="pt-4">
      Aqui segue algumas indicações de filmes
    </v-card-subtitle>

    <v-card-text>
      <div>textinho aqui</div>

      <div>Aqui tbm</div>
    </v-card-text>

    <v-card-actions>
      <v-btn color="orange">
        Share
      </v-btn>

      <v-btn color="orange">
        Ver filmes
      </v-btn>
    </v-card-actions>
  </v-card>

</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import resultadoApi from "@/api/resultado.api"

export default {
data () {
    return {
    show: false,
    horario: '',
    planta: '',
    bebida: '',
    resultado: ''
    }
},
computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
},
mounted() {
    this.getResultado()
  },
  methods: {
    getResultado() {
      this.loading = true
      resultadoApi.getResultado().then((data) => {
        this.resultado = data.todos[0]
        console.log(this.resultado)
        this.loading = false
      })
    },
    }
}
</script>

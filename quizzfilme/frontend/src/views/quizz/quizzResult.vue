<template>
  <div>
  <v-card
    class="mx-auto mt-10"
    max-width="900"
  >
    <v-img
      class="align-end text-white"
      height="200"
      src="https://media.istockphoto.com/id/1350788409/photo/pink-color-background.jpg?b=1&s=170667a&w=0&k=20&c=w2q6NV8dHpNIWpYpq_capQau6-RDNoJepXXMhRH5ySo="
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

      <v-btn color="orange" @click="showfilmes()">
        Ver filmes
      </v-btn>
    </v-card-actions>
    <v-window
    v-if="show"
    v-model="window"
    show-arrows
  >
    <v-window-item
      v-for="n in length"
      :key="n"
    >
      <v-card height="200px" class="d-flex justify-center align-center">
        <span class="text-h2">Card {{ n }}</span>
      </v-card>
    </v-window-item>
  </v-window>
  </v-card>

</div>
  
</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import resultadoApi from "@/api/resultado.api"

export default {
data () {
    return {
    show: false,
    resultado: '',
    length: 3,
    window: 0,
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
      resultadoApi.getResultado(this.loggedUser).then((data) => {
        this.resultado = data.todos[0]
        console.log(this.resultado)
        this.loading = false
      })
    },
    showfilmes(){
      if (this.show === true){
        this.show = false
      }else{
        this.show=true
      }
    }
    }
}
</script>

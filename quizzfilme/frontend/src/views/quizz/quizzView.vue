<template>
    <div>
        <v-card
            class="mx-auto mt-5"
            color="deep-purple darken-4"
            dark
            max-width="900">
            <v-card-title>
            <span class="text-h6 font-weight-light">Qual sua cor favorita?</span>
            </v-card-title>
                <v-radio-group v-model="cor">
                    <v-radio label="Vermelho" value="a"></v-radio>
                    <v-radio label="rosa" value="b1"></v-radio>
                    <v-radio label="preto" value="a1"></v-radio>
                    <v-radio label="verde" value="c"></v-radio>
                    <v-radio label="roxo" value="c1"></v-radio>
                    <v-radio label="laranja" value="b"></v-radio>
                </v-radio-group>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            color="deep-purple darken-4"
            dark
            max-width="900">
            <v-card-title>
            <span class="text-h6 font-weight-light">Rápido! pose pra a foto!</span>
            </v-card-title>
                <v-radio-group v-model="foto">
                    <v-radio label="Hang Loose" value="c1"></v-radio>
                    <v-radio label="Coloca a língua pra fora" value="a"></v-radio>
                    <v-radio label="sorri" value="b1"></v-radio>
                    <v-radio label="Não faz nada" value="a1"></v-radio>
                    <v-radio label="peace fingers" value="b"></v-radio>
                    <v-radio label="congela" value="c"></v-radio>
                </v-radio-group>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            color="deep-purple darken-4"
            dark
            max-width="900">
            <v-card-title>
            <span class="text-h6 font-weight-light">Qual seu animal favorito</span>
            </v-card-title>
                <v-radio-group v-model="animal">
                    <v-radio label="cobra" value="a"></v-radio>
                    <v-radio label="coelho" value="b1"></v-radio>
                    <v-radio label="hamster" value="b"></v-radio>
                    <v-radio label="gato" value="a1"></v-radio>
                    <v-radio label="sapo" value="c"></v-radio>
                    <v-radio label="cachorro" value="c1"></v-radio>
                </v-radio-group>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            color="deep-purple darken-4"
            dark
            max-width="900">
            <v-card-title>
            <span class="text-h6 font-weight-light">Como você mataria alguém?</span>
            </v-card-title>
                <v-radio-group v-model="mataria">
                    <v-radio label="Enforcando" value="a"></v-radio>
                    <v-radio label="Atirando" value="b1"></v-radio>
                    <v-radio label="Nunca faria isso" value="b"></v-radio>
                    <v-radio label="Empurrando de um lugar alto" value="c"></v-radio>
                    <v-radio label="Atropelando" value="c1"></v-radio>
                    <v-radio label="Esfaqueando" value="a1"></v-radio>
                </v-radio-group>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            color="deep-purple darken-4"
            dark
            max-width="900">
            <v-card-title>
            <span class="text-h6 font-weight-light">Qual sua bebida favorita?</span>
            </v-card-title>
                <v-radio-group v-model="bebida">
                    <v-radio label="leite" value="b1"></v-radio>
                    <v-radio label="suco" value="b"></v-radio>
                    <v-radio label="cerveja" value="c1"></v-radio>
                    <v-radio label="coca-cola" value="c"></v-radio>
                    <v-radio label="café" value="a"></v-radio>
                    <v-radio label="vinho" value="a1"></v-radio>
                </v-radio-group>
            </v-card>
        <v-card
        class="d-flex justify-center mx-auto mt-5 mb-5"
        color="deep-purple darken-4"
        dark
        max-width="900">
            <v-btn @click="contabilizarRespostas()"
             class=" mt-5 mb-5"
             color="deep-purple accent-4">
                Submit
            </v-btn>
        </v-card>
            
            
        
    </div>
</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import resultadoApi from "@/api/resultado.api.js"

export default {
data () {
    return {
    cor: '',
    foto: '',
    animal:'',
    mataria: '',
    bebida:'',

    }
},
computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
},
methods: {
    contabilizarRespostas(){
        let respostas = []
        respostas.push(this.cor, this.foto, this.animal, this.mataria, this.bebida)
        console.log(this.loggedUser)
        this.salvarResultado(respostas)
        return respostas
    },
    salvarResultado(resultado){
        this.loading = true
      resultadoApi.addNewResultado(resultado, this.loggedUser.id).then((resultado) => {
        this.loading = false
        this.$router.push({ name: "resultado" })
        console.log(resultado)
      }) .catch((error) => {
            console.log('ferrou')
            this.loading = false
        })

    }
},
}
</script>

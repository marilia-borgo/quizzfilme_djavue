<template>
    <div>
        <p> Qual sua cor favorita?</p>
        <v-radio-group v-model="cor">
            <v-radio label="Vermelho" value="a"></v-radio>
            <v-radio label="rosa" value="b"></v-radio>
            <v-radio label="preto" value="a"></v-radio>
            <v-radio label="verde" value="c"></v-radio>
            <v-radio label="roxo" value="c"></v-radio>
            <v-radio label="laranja" value="b"></v-radio>
        </v-radio-group>

        <p> Rapido! pose pra a foto!</p>
        <v-radio-group v-model="foto">
            <v-radio label="Hang Loose" value="c"></v-radio>
            <v-radio label="Coloca a língua pra fora" value="a"></v-radio>
            <v-radio label="sorri" value="b"></v-radio>
            <v-radio label="Não faz nada" value="a"></v-radio>
            <v-radio label="peace fingers" value="b"></v-radio>
            <v-radio label="congela" value="c"></v-radio>
        </v-radio-group>

        <p> Qual seu animal favorito?</p>
        <v-radio-group v-model="animal">
            <v-radio label="cobra" value="a"></v-radio>
            <v-radio label="coelho" value="b"></v-radio>
            <v-radio label="hamster" value="b"></v-radio>
            <v-radio label="gato" value="a"></v-radio>
            <v-radio label="sapo" value="c"></v-radio>
            <v-radio label="cachorro" value="c"></v-radio>
        </v-radio-group>

        <p> Como você mataria alguém?</p>
        <v-radio-group v-model="mataria">
            <v-radio label="Enforcando" value="a"></v-radio>
            <v-radio label="Atirando" value="b"></v-radio>
            <v-radio label="Nunca faria isso" value="b"></v-radio>
            <v-radio label="Empurrando de um lugar alto" value="c"></v-radio>
            <v-radio label="Atropelando" value="c"></v-radio>
            <v-radio label="Esfaqueando" value="a"></v-radio>
        </v-radio-group>

        <p> Qual sua bebida favorita?</p>
        <v-radio-group v-model="bebida">
            <v-radio label="leite" value="b"></v-radio>
            <v-radio label="suco" value="b"></v-radio>
            <v-radio label="cerveja" value="c"></v-radio>
            <v-radio label="coca-cola" value="c"></v-radio>
            <v-radio label="café" value="a"></v-radio>
            <v-radio label="vinho" value="a"></v-radio>
        </v-radio-group>
        <v-btn @click="contabilizarRespostas()">
            Submit
        </v-btn>
    </div>
</template>
  
<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import tratamentoQuizz from "@/helpers/tratamentoQuizz.js"
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
        console.log(respostas)
        let result = tratamentoQuizz.defineLetra(respostas)
        this.salvarResultado(result)
        return result
    },
    salvarResultado(resultado){
        this.loading = true
      resultadoApi.addNewResultado(resultado).then((resultado) => {
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

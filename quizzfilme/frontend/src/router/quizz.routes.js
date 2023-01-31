// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import QuizzView from "@/views/quizz/quizzView.vue"
import QuizzResult from "@/views/quizz/quizzResult.vue"

export default [
  {
    path: "/quizz",
    component: DefaultLayout,
    children: [
      {
        path: "",
        name: "quizz",
        component: QuizzView,
      },
      {
        path: "resultado",
        name: "resultado",
        component: QuizzResult,
      },
    ],
  },
]

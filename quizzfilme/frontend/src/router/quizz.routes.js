// Composables
import DefaultLayout from "@/layouts/default/DefaultLayout.vue"
import QuizzView from "@/views/quizz/quizzView.vue"

export default [
  {
    path: "/quizz",
    component: DefaultLayout,
    children: [
      {
        path: "quizz",
        name: "quizz",
        component: QuizzView,
      },
    ],
  },
]

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HelloDialogComponent} from './hello-dialog/hello-dialog.component';
import {EkranComponent} from './ekran/ekran.component';
import {ReadmeComponent} from './readme/readme.component';
import {GenerateComponent} from './generate/generate.component';
import {GenerateBadComponent} from './generate-bad/generate-bad.component';
import {EkranWynikowComponent} from './ekran-wynikow/ekran-wynikow.component';

const routes: Routes = [
  { path: 'start', component: HelloDialogComponent },
  { path: 'game',      component: EkranComponent },
  { path: 'solution',      component: EkranWynikowComponent },
  { path: 'generate',      component: GenerateComponent },
  {path: 'bad_generate', component: GenerateBadComponent},
  { path: 'readme',      component: ReadmeComponent },

  { path: '',
    redirectTo: '/start',
    pathMatch: 'full'
  },
  { path: '**', component: HelloDialogComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

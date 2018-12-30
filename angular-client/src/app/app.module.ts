import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HelloDialogComponent } from './hello-dialog/hello-dialog.component';
import {FormsModule} from '@angular/forms';
import { WidokComponent } from './widok/widok.component';
import { MenuBComponent } from './menu-b/menu-b.component';
import { WynikGraczaComponent } from './wynik-gracza/wynik-gracza.component';
import { WynikDanychComponent } from './wynik-danych/wynik-danych.component';
import {HttpClientModule} from '@angular/common/http';
import { EkranComponent } from './ekran/ekran.component';
import { ReadmeComponent } from './readme/readme.component';
import { GenerateComponent } from './generate/generate.component';
import { GenerateBadComponent } from './generate-bad/generate-bad.component';
import { EkranWynikowComponent } from './ekran-wynikow/ekran-wynikow.component';
import { NewGameComponent } from './new-game/new-game.component';
import { OkienkoNowaGRaComponent } from './okienko-nowa-gra/okienko-nowa-gra.component';

@NgModule({
  declarations: [
    AppComponent,
    HelloDialogComponent,
    WidokComponent,
    MenuBComponent,
    WynikGraczaComponent,
    WynikDanychComponent,
    EkranComponent,
    ReadmeComponent,
    GenerateComponent,
    GenerateBadComponent,
    EkranWynikowComponent,
    NewGameComponent,
    OkienkoNowaGRaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

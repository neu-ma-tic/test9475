package main

import (
	"fmt"
	"html"
	"log"
	"net/http"
	"os"
	"os/signal"
	"strings"
	"syscall"
	"time"

	embed "github.com/Clinet/discordgo-embed"
	"github.com/bwmarrin/discordgo"
	dotenv "github.com/joho/godotenv"
)

func main() {

	// Create a new Discord session using the provided bot token.
	token := os.Getenv("TOKEN")

	if token == "" {
		err := dotenv.Load(".env")
		if err != nil {
			panic("Cannot start server, no token available")
		}
		token = os.Getenv("TOKEN")
	}

	dg, err := discordgo.New("Bot " + token)
	if err != nil {
		fmt.Println("error creating Discord session,", err)
		return
	}

	// Register the messageCreate func as a callback for MessageCreate events.
	dg.AddHandler(messageCreate)

	// In this example, we only care about receiving message events.
	dg.Identify.Intents = discordgo.IntentsGuildMessages

	// Open a websocket connection to Discord and begin listening.
	err = dg.Open()
	if err != nil {
		fmt.Println("error opening connection,", err)
		return
	}

	// Wait here until CTRL-C or other term signal is received.
	fmt.Println("Bot is now running.  Press CTRL-C to exit.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
	<-sc

	http.HandleFunc("/bar", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
	})

	log.Fatal(http.ListenAndServe(":8080", nil))

	// Cleanly close down the Discord session.
	dg.Close()
}

// This function will be called (due to AddHandler above) every time a new
// message is created on any channel that the authenticated bot has access to.
func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {

	// Ignore all messages created by the bot itself
	// This isn't required in this specific example but it's a good practice.
	if m.Author.ID == s.State.User.ID {
		return
	}
	// If the message is "ping" reply with "Pong!"
	if m.Content == "ping" {
		s.ChannelMessageSend(m.ChannelID, "Pong!")
	}

	// If the message is "pong" reply with "Ping!"
	if m.Content == "pong" {
		s.ChannelMessageSend(m.ChannelID, "Ping!")
	}

	if strings.ToLower(m.Content) == "no" {
		s.ChannelMessageSend(m.ChannelID, "Ha Get Rekt noob!")
	}

	if strings.ToLower(m.Content) == "bruh" {
		imgEmbed := embed.NewEmbed().SetImage("https://biographyhub.com/wp-content/uploads/2021/04/Arsenal-RL.jpg").MessageEmbed
		s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)
	}

	if strings.EqualFold(m.Content, "Who's the best?") {
		imgEmbed := embed.NewEmbed().SetTitle("Ya boi is da best, ya feel me!").SetImage("https://images2.minutemediacdn.com/image/upload/c_fill,w_720,ar_16:9,f_auto,q_auto,g_auto/shape/cover/sport/dataimagewebpbase64UklGRraHAABXRUJQVlA4IKqHAADwjwK-7debd14d7c6b7af842fbb2af6a2b701e.jpg").MessageEmbed
		s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)
	}

	if strings.EqualFold(m.Content, "Kill me") {
		imgEmbed := embed.NewEmbed().SetImage("https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1459980594i/18682005.jpg").MessageEmbed
		s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)
	}

	if strings.EqualFold(m.Content, "Arsenal Close") {
		if isAdmin(&m.Author.ID) {
			s.ChannelMessageSend(m.ChannelID, "Bot closing in 2 seconds")
			time.Sleep(2 * time.Second)
			panic("Program terminated by admin")

		} else {
			s.ChannelMessageSend(m.ChannelID, ("You don't have permission to use this command " + m.Author.Mention()))

		}
	}

	if strings.ToLower(m.Content) == "arbb" {
		s.ChannelMessageDelete(m.ChannelID, m.ID)
		if isAdmin(&m.Author.ID) {

			imgEmbed := embed.NewEmbed().SetImage("https://c.tenor.com/QaGZ50VlEPEAAAAM/think-about-it-use-your-brain.gif").MessageEmbed
			s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)

		} else {
			imgEmbed := embed.NewEmbed().SetImage("https://www.sbs.com.au/guide/sites/sbs.com.au.guide/files/styles/body_image/public/brain_leaves.gif?itok=S_hKrg8V&mtime=1470115287").MessageEmbed
			s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)
		}

	}
	if strings.ToLower(m.Content) == "cute" {
		imgEmbed := embed.NewEmbed().SetImage("https://media1.tenor.com/images/7052bc22327a608efe27f343ab6c0142/tenor.gif").MessageEmbed

		s.ChannelMessageSendEmbed(m.ChannelID, imgEmbed)
	}
}

func isAdmin(au *string) bool {
	if *au == "385922547591675905" {
		return true
	}
	return false
}
